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

from flask import json

import main


def test_index():
    main.app.testing = True
    client = main.app.test_client()

    req = {
      "responseId": "ea3d77e8-ae27-41a4-9e1d-174bd461b68c",
      "session": "projects/your-agents-project-id/agent/sessions/88d13aa8-2999-4f71-b233-39cbf3a824a0",
      "queryResult": {
        "queryText": "user's original query to your agent",
        "parameters": {
            "param": "param value"
        },
        "allRequiredParamsPresent": True,
        "fulfillmentText": "Text defined in Dialogflow's console for the intent that was matched",
        "fulfillmentMessages": [
          {
            "text": {
              "text": [
                "Text defined in Dialogflow's console for the intent that was matched"
              ]
            }
          }
        ],
        "outputContexts": [
          {
            "name": "projects/your-agents-project-id/agent/sessions/88d13aa8-2999-4f71-b233-39cbf3a824a0/contexts/",
            "lifespanCount": 5,
            "parameters": {
              "param": "param value"
            }
          }
        ],
        "intent": {
          "name": "projects/your-agents-project-id/agent/intents/29bcd7f8-f717-4261-a8fd-2d3e451b8af8",
          "displayName": "Matched Intent Name"
        },
        "intentDetectionConfidence": 1,
        "diagnosticInfo": {},
        "languageCode": "en"
      },
      "originalDetectIntentRequest": {}
    }

    res = client.post('/', content_type='application/json', data=json.dumps(req))
    data = json.loads(res.get_data().decode("utf-8"))

    assert res.status_code == 200
    assert data['fulfillmentText'] == 'Please send me a file'

#
# def test_file_upload():
#     main.app.testing = True
#     client = main.app.test_client()
#
#     data = {
#         'file': '/home/gmariotti/repos/python-transcription-app/tests/resources/AUDIO-2019-01-19-14-57-47.opus'
#     }
#
#     res = client.post('/', data=data)
#     assert res.status_code == 200
