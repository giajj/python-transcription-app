
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

import io
import logging
from flask import Flask, request, jsonify, make_response
from ast import literal_eval
import datetime

from bot.transcription import speech_to_text
from bot.storage import upload_file


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
    @app.route("/")
    def index():
        return 'This Bot only works with post requests'

    @app.route('/', methods=['POST'])
    def post_request():
        app.logger.info('Content-Type: %s', request.headers['Content-Type'])
        try:
            if 'file' in request.files:
                add_request()
                file = request.files['file']

                app.logger.info('Call transcription service')
                with io.open(file, 'rb') as audio_file:
                    content = audio_file.read()
                    fulfillment_text = speech_to_text(content)
                context = literal_eval(request.form.get('queryResult'))['outputContexts']

            else:
                fulfillment_text = 'Please send me a file'
                context = request.get_json(force=True)['queryResult']['outputContexts']

            # Response to send to Dialogflow
            res = {
                "fulfillmentText": fulfillment_text,
                'outputContexts': context
            }
        except Exception as e:
            app.logger.info('ERROR: %s', e)
            res = {"fulfillmentText": 'ERROR'}
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


def add_request():
    data = request.form.to_dict(flat=True)
    file_url = upload_file(request.files.get('file'))

    db_data = {
        'id': data['responseId'],
        'user': 'NA',
        'timestamp': str(datetime.datetime.utcnow()),
        'query_text': literal_eval(data['queryResult'])['queryText'],
        'file_url': file_url
    }

    bot_request = get_model().create(db_data)

    return bot_request
