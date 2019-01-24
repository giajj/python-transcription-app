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

# [START gae_python37_app]
from flask import Flask, request, jsonify, make_response


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
FALLBACK_RESPONSE = 'Please send me an audio file to transcribe'


@app.route('/', methods=['POST'])
def post_request():
    app.logger.info('Content-Type: %s', request.headers['Content-Type'])
    req = request.get_json(force=True)

    # Response to send to Dialogflow
    res = {
        "fulfillmentText": FALLBACK_RESPONSE,
        'outputContexts': req['queryResult']['outputContexts']
    }

    return make_response(jsonify(res))


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
