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
from flask import json

import main

TEST_REQ = {
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


def test_post_no_file():
    main.app.testing = True
    client = main.app.test_client()

    res = client.post('/', content_type='application/json', data=json.dumps(TEST_REQ))
    data = json.loads(res.get_data().decode("utf-8"))

    assert res.status_code == 200
    assert data['fulfillmentText'] == 'Please send me a file'


def test_post_file():
    main.app.testing = True
    client = main.app.test_client()

    data = TEST_REQ
    data = {key: str(value) for key, value in data.items()}
    data['file'] = (io.BytesIO(b"abcdef"), 'test.jpg')

    res = client.post('/', data=data, content_type='multipart/form-data')
    assert res.status_code == 200


# def runTest(self):
#     with open(self.dir + '/img/img1.jpg', 'rb') as img1:
#         img1StringIO = StringIO(img1.read())
#
#     response = self.app.post('/convert',
#                              content_type='multipart/form-data',
#                              data={'photo': (img1StringIO, 'img1.jpg')},
#                              follow_redirects=True)
#     img1StringIO.seek(0)
#     assert response.data == imgStringIO.read()
#
# def test_edit_logo(self):
#     """Test can upload logo."""
#     data = {'name': 'this is a name', 'age': 12}
#     data = {key: str(value) for key, value in data.items()}
#     data['file'] = (io.BytesIO(b"abcdef"), 'test.jpg')
#     self.login()
#     response = self.client.post(
#         url_for('adverts.save'), data=data, follow_redirects=True,
#         content_type='multipart/form-data'
#     )
#     self.assertIn(b'Your item has been saved.', response.data)
#     advert = Item.query.get(1)
#     self.assertIsNotNone(item.logo)