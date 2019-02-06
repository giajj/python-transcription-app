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

sample_facebook_text_request = {
   "responseId": "c8c14a13-7797-4de2-b6df-f25dfbb58dff",
   "queryResult": {
      "queryText": "text only",
      "action": "input.unknown",
      "parameters": {

      },
      "allRequiredParamsPresent": True,
      "fulfillmentMessages": [
         {
            "text": {
               "text": [
                  ""
               ]
            }
         }
      ],
      "outputContexts": [
         {
            "name": "projects/pristine-atom-226517/agent/sessions/6fa3c1fe-6573-48b4-8ad1-d9ce2e71fc27/contexts/defaultfallbackintent-followup",
            "lifespanCount": 2
         },
         {
            "name": "projects/pristine-atom-226517/agent/sessions/6fa3c1fe-6573-48b4-8ad1-d9ce2e71fc27/contexts/generic",
            "lifespanCount": 4,
            "parameters": {
               "facebook_sender_id": "2109732695780744"
            }
         }
      ],
      "intent": {
         "name": "projects/pristine-atom-226517/agent/intents/d4032e6d-d2a7-4659-931e-f12ef17ca2da",
         "displayName": "Default Fallback Intent",
         "isFallback": True
      },
      "intentDetectionConfidence": 1.0,
      "languageCode": "en"
   },
   "originalDetectIntentRequest": {
      "source": "facebook",
      "payload": {
         "data": {
            "sender": {
               "id": "2109732695780744"
            },
            "recipient": {
               "id": "590108701452104"
            },
            "message": {
               "mid": "6x2c3BEj9RemIkZL7bNPEaIP7U1RzGN2MLu2WlPcaUW2gtydHgtHTeCve8cK-yyHjCYoAb2YJ0Q_UOOpV4pqRg",
               "text": "text only",
               "seq": 24795.0
            },
            "timestamp": 1548705494847.0
         },
         "source": "facebook"
      }
   },
   "session": "projects/pristine-atom-226517/agent/sessions/6fa3c1fe-6573-48b4-8ad1-d9ce2e71fc27"
}

sample_facebook_flac_request_en = {  
   "responseId": "91c6315c-81c5-425e-bcdf-9793ba1e89c9",
   "queryResult": {  
      "queryText": "FACEBOOK_MEDIA",
      "parameters": {  

      },
      "allRequiredParamsPresent": True,
      "fulfillmentMessages": [  
         {  
            "text": {  
               "text": [  
                  ""
               ]
            }
         }
      ],
      "outputContexts": [  
         {  
            "name": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5/contexts/transcription-language-followup",
            "lifespanCount": 1,
            "parameters": {  
               "language.original": "English",
               "language": "English"
            }
         },
         {  
            "name": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5/contexts/facebook_media"
         },
         {  
            "name": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5/contexts/transcription-followup",
            "parameters": {  
               "language.original": "English",
               "language": "English"
            }
         },
         {  
            "name": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5/contexts/defaultfallbackintent-followup",
            "lifespanCount": 2
         },
         {  
            "name": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5/contexts/generic",
            "lifespanCount": 4,
            "parameters": {  
               "language.original": "English",
               "language": "English",
               "facebook_sender_id": "2109732695780744"
            }
         }
      ],
      "intent": {  
         "name": "projects/pristine-atom-226517/agent/intents/d4032e6d-d2a7-4659-931e-f12ef17ca2da",
         "displayName": "Default Fallback Intent",
         "isFallback": True
      },
      "intentDetectionConfidence": 1.0,
      "languageCode": "en"
   },
   "originalDetectIntentRequest": {  
      "source": "facebook",
      "payload": {  
         "data": {  
            "sender": {  
               "id": "2109732695780744"
            },
            "recipient": {  
               "id": "590108701452104"
            },
            "message": {  
               "attachments": [  
                  {  
                     "payload": {  
                        "url": "https://cdn.fbsbx.com/v/t59.3654-21/15308171_1226846694027684_8966586941638180864_n.flac/brooklyn.flac?_nc_cat=101&_nc_ht=cdn.fbsbx.com&oh=169a33f28b5910bbc958dcc81f70a6d6&oe=5C5CE0AA"
                     },
                     "type": "audio"
                  }
               ],
               "mid": "-jkTxYFQhiky7QQiYWv-vKIP7U1RzGN2MLu2WlPcaUXluY2OrADduGShlIwSFA_4bPcYyOBE1kxkzmx9OC8urw",
               "seq": 25094.0
            },
            "timestamp": 1548846699363.0
         },
         "source": "facebook"
      }
   },
   "session": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5"
}

sample_facebook_opus_request_en = {
   "responseId": "ed38a143-6ce7-4f7c-b84f-8973c3aa483a",
   "queryResult": {
      "queryText": "FACEBOOK_MEDIA",
      "parameters": {

      },
      "allRequiredParamsPresent": True,
      "fulfillmentMessages": [
         {
            "text": {
               "text": [
                  ""
               ]
            }
         }
      ],
      "outputContexts": [
         {
            "name": "projects/pristine-atom-226517/agent/sessions/3d1922c 3-f788-4747-b086-4c4263fdb1e5/contexts/transcription-language-followup",
            "lifespanCount": 1,
            "parameters": {
               "language.original": "English",
               "language": "English"
            }
         },
         {
            "name": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5/contexts/facebook_media"
         },
         {
            "name": "projects/pristine-atom- 226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5/contexts/transcription-followup",
            "parameters": {
               "language.original": "English",
               "language": "English"
            }
         },
         {
            "name": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5/contexts/defaultfallbackintent-followup",
            "lifespanCount": 2
         },
         {
            "name": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5/contexts/generic",
            "lifespanCount": 4,
            "parameters": {
               "language.original": "English",
               "language": "English",
               "facebook_sender_id": "2109732695780744"
            }
         }
      ],
      "intent": {
         "name": "projects/pristine-atom-226517/agent/intents/d403 2e6d-d2a7-4659-931e-f12ef17ca2da",
         "displayName": "Default Fallback Intent",
         "isFallback": True
      },
      "intentDetectionConfidence": 1.0,
      "languageCode": "en"
   },
   "originalDetectIntentRequest": {
      "source": "facebook",
      "payload": {
         "data": {
            "sender": {
               "id": "2109732695780744"
            },
            "recipient": {
               "id": "590108701452104"
            },
            "message": {
               "attachments": [
                  {
                     "payload": {
                        "url": "https://cdn.fbsbx.com/v/t59.2708-21/50203080_2581615095187609_8740172015438135296_n.opus/AUDIO-2019-01-29-16-59-57.opus?_nc_cat=100&_nc_ht=cdn.fbsbx.com&oh=95dc3661d0625d96e6439f935f4db055&oe=5C5D274D"
                     },
                     "type": "file"
                  }
               ],
               "mid": "WWBKWDfXTIKl9uZv0wVnwqIP7U1RzGN2MLu2WlPcaUVBdhM j3ocJUoGMm89ttSCO4cVC5Hs_D6p6kNASbR3I6Q",
               "seq": 25072.0
            },
            "timestamp": 1548846543812.0
         },
         "source": "facebook"
      }
   },
   "session": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5"
}


sample_facebook_opus_request_it = {  
   "responseId": "14ac088e-e689-4c62-af7f-07f1df0ec962",
   "queryResult": {
      "queryText": "FACEBOOK_MEDIA",
      "parameters": {

      },
      "allRequiredParamsPresent": True,
      "fulfillmentMessages": [
         {
            "text": {
               "text": [
                  ""
               ]
            }
         }
      ],
      "outputContexts": [
         {
            "name": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5/contexts/transcription-language-followup",
            "lifespanCount": 1,
            "parameters": {
               "language.original": "Italian",
               "language": "Italian"
            }
         },
         {
            "name": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5/contexts/facebook_media"
         },
         {
            "name": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5/contexts/transcription-followup",
            "parameters": {
               "language.original": "Italian",
               "language": "Italian"
            }
         },
         {
            "name": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5/contexts/defaultfallbackintent-followup",
            "lifespanCount": 2
         },
         {
            "name": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5/contexts/generic",
            "lifespanCount": 4,
            "parameters": {
               "language.original": "Italian",
               "language": "Italian",
               "facebook_sender_id": "2109732695780744"
            }
         }
      ],
      "intent": {
         "name": "projects/pristine-atom-226517/agent/intents/d4032e6d-d2a7-4659-931e-f12ef17ca2da",
         "displayName": "Default Fallback Intent",
         "isFallback": True
      },
      "intentDetectionConfidence": 1.0,
      "languageCode": "en"
   },
   "originalDetectIntentRequest": {
      "source": "facebook",
      "payload": {
         "data": {
            "sender": {
               "id": "2109732695780744"
            },
            "recipient": {
               "id": "590108701452104"
            },
            "message": {
               "attachments": [
                  {
                     "payload": {
                        "url": "https://cdn.fbsbx.com/v/t59.2708-21/51190382_597970917343490_2531532000041369600_n.opus/AUDIO-2019-01-30-08-45-16.opus?_nc_cat=111&_nc_ht=cdn.fbsbx.com&oh=a1cb16a5de889fbcce21557479453e64&oe=5C5D4BEC"
                     },
                     "type": "file"
                  }
               ],
               "mid": "EoAJjojdyMAWR6YQayTl-6IP7U1RzGN2MLu2WlPcaUVus69D9Z17UXYOsKjnOcThlYut7rRL_LcXSX5ZjMwRBw",
               "seq": 25051.0
            },
            "timestamp": 1548846301655.0
         },
         "source": "facebook"
      }
   },
   "session": "projects/pristine-atom-226517/agent/sessions/3d1922c3-f788-4747-b086-4c4263fdb1e5"
}
