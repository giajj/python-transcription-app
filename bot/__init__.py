# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from flask import Flask, request, jsonify, make_response, current_app
import datetime

from bot.transcription import speech_to_text
from bot.storage import upload_file, upload_from_url

DEFAULT_LANGUAGE_CODE = 'en-US'


def create_app(config, debug=False, testing=False, config_overrides=None):
    app = Flask(__name__)
    app.config.from_object(config)

    app.debug = debug
    app.testing = testing

    if config_overrides:
        app.config.update(config_overrides)

    # Configure logging
    if not app.testing:
        logging.basicConfig(level=logging.INFO)

    # Setup the data model.
    with app.app_context():
        model = get_model()
        model.init_app(app)

    # Add a default root route.
    @app.route('/')
    def index():
        return 'This Bot only works with post requests'

    @app.route('/', methods=['POST'])
    def post_request():
        app.logger.info('Content-Type: %s', request.headers['Content-Type'])
        request_json = request.get_json(force=True)

        saved_request = save_request(request_json)
        app.logger.info('Request saved in database')

        if is_transcription_language_followup(request_json['queryResult']['outputContexts']):
            try:
                if saved_request['file_type'] in ['audio', 'file']:
                    app.logger.info('Call transcription service')
                    language_code = get_speech_language(request_json['queryResult']['outputContexts'])
                    fulfillment_text = speech_to_text(saved_request['bucket_file_url'], language_code)
                else:
                    fulfillment_text = 'Please send me an audio file'
            except Exception as e:
                app.logger.info('ERROR: %s', e)
                fulfillment_text = 'There was an error in processing your transcription'
        else:
            fulfillment_text = 'Request not recognised. Please say "Hi" to begin again.'

        app.logger.info('Sending response to Dialogflow')
        res = {
            'fulfillmentText': fulfillment_text,
            'outputContexts': request_json['queryResult']['outputContexts']
        }
        return make_response(jsonify(res))

    # Add an error handler. This is useful for debugging the live application,
    # however, you should disable the output of the exception for production
    # applications.
    @app.errorhandler(500)
    def server_error(e):
        return """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500

    return app


def get_model():
    from . import model_cloudsql
    return model_cloudsql


def save_request(request_json):
    message = request_json['originalDetectIntentRequest']['payload']['data']['message']

    id = request_json['responseId']
    user = request_json['queryResult']['outputContexts'][-1]['parameters']['facebook_sender_id']
    timestamp = str(datetime.datetime.utcnow())
    query_text = request_json['queryResult']['queryText']

    original_file_url = bucket_file_url = file_type = ''

    if 'attachments' in message:
        original_file_url = message['attachments'][0]['payload']['url']
        bucket_file_url = upload_from_url(original_file_url)
        file_type = message['attachments'][0]['type']

    db_data = {
        'id': id,
        'user': user,
        'timestamp': timestamp,
        'query_text': query_text,
        'original_file_url': original_file_url,
        'bucket_file_url': bucket_file_url,
        'file_type': file_type,
        'json': str(request_json)
    }

    return get_model().create(db_data)


def is_transcription_language_followup(context):
    for interaction in context:
        if 'transcription-language-followup' in interaction['name']:
            return True
    return False


def get_speech_language(context):
    for interaction in context:
        if 'transcription-language-followup' in interaction['name']:
            return get_language_code(interaction['parameters']['language'])

    current_app.logger.info(
        'ERROR: Language information not found in context. Using default (%s)', DEFAULT_LANGUAGE_CODE)
    return DEFAULT_LANGUAGE_CODE


def get_language_code(language):
    if language.lower() == 'italian':
        return 'it-IT'
    elif language.lower() == 'english':
        return 'en-US'
    else:
        current_app.logger.info(
            'ERROR: Language information not found in context. Using default (%s)', DEFAULT_LANGUAGE_CODE)
        return DEFAULT_LANGUAGE_CODE
