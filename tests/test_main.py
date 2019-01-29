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
import random

import main
from tests.sample_requests import sample_facebook_text_request, sample_facebook_flac_request, \
    sample_facebook_opus_request


def test_post_facebook_text():
    main.app.testing = True
    client = main.app.test_client()

    sample_facebook_text_request['responseId'] += str(random.getrandbits(128))

    res = client.post('/', content_type='application/json', data=json.dumps(sample_facebook_text_request))
    data = json.loads(res.get_data().decode("utf-8"))

    assert res.status_code == 200
    assert data['fulfillmentText'] == 'Please send me an audio file'


def test_post_facebook_flac():
    main.app.testing = True
    client = main.app.test_client()

    sample_facebook_flac_request['responseId'] += str(random.getrandbits(128))

    res = client.post('/', content_type='application/json', data=json.dumps(sample_facebook_flac_request))
    data = json.loads(res.get_data().decode("utf-8"))

    assert res.status_code == 200
    assert data['fulfillmentText'] == 'how old is the Brooklyn Bridge'


def test_post_facebook_opus():
    main.app.testing = True
    client = main.app.test_client()

    sample_facebook_flac_request['responseId'] += str(random.getrandbits(128))

    res = client.post('/', content_type='application/json', data=json.dumps(sample_facebook_opus_request))
    data = json.loads(res.get_data().decode("utf-8"))

    assert res.status_code == 200
    assert data['fulfillmentText'] == 'how old is the Brooklyn Bridge'
