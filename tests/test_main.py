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
from tests.sample_requests import sample_facebook_text_request, sample_facebook_flac_request_en, \
    sample_facebook_opus_request_en, sample_facebook_opus_request_it


def test_post_facebook_text():
    main.app.testing = True
    client = main.app.test_client()

    sample_facebook_text_request['responseId'] += str(random.getrandbits(128))

    res = client.post('/', content_type='application/json', data=json.dumps(sample_facebook_text_request))
    data = json.loads(res.get_data().decode("utf-8"))

    assert res.status_code == 200
    assert data['fulfillmentText'] == 'Request not recognised. Please say "Hi" to begin again.'


def test_post_facebook_flac_en():
    main.app.testing = True
    client = main.app.test_client()

    sample_facebook_flac_request_en['responseId'] += str(random.getrandbits(128))

    res = client.post('/', content_type='application/json', data=json.dumps(sample_facebook_flac_request_en))
    data = json.loads(res.get_data().decode("utf-8"))

    assert res.status_code == 200
    assert data['fulfillmentText'].lower() == 'how old is the brooklyn bridge'


def test_post_facebook_opus_en():
    main.app.testing = True
    client = main.app.test_client()

    sample_facebook_opus_request_en['responseId'] += str(random.getrandbits(128))

    res = client.post('/', content_type='application/json', data=json.dumps(sample_facebook_opus_request_en))
    data = json.loads(res.get_data().decode("utf-8"))

    assert res.status_code == 200
    assert data['fulfillmentText'].lower() == 'how old is the brooklyn bridge'


def test_post_facebook_opus_it():
    main.app.testing = True
    client = main.app.test_client()

    sample_facebook_opus_request_it['responseId'] += str(random.getrandbits(128))

    res = client.post('/', content_type='application/json', data=json.dumps(sample_facebook_opus_request_it))
    data = json.loads(res.get_data().decode("utf-8"))

    assert res.status_code == 200
    assert data['fulfillmentText'].lower() == 'quanti anni ha il ponte della vittoria'
