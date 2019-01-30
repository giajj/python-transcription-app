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
   "responseId": "e5439946-24f5-4995-85be-4f36b9d96b3a",
   "queryResult": {  
      "queryText": "FACEBOOK_MEDIA",
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
            "name": "projects/pristine-atom-226517/agent/sessions/7128851b-8967-49f6-8f04-8a86ca97137d/contexts/facebook_media"
         },
         {  
            "name": "projects/pristine-atom-226517/agent/sessions/7128851b-8967-49f6-8f04-8a86ca97137d/contexts/defaultfallbackintent-followup",
            "lifespanCount": 2
         },
         {  
            "name": "projects/pristine-atom-226517/agent/sessions/7128851b-8967-49f6-8f04-8a86ca97137d/contexts/generic",
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
               "attachments": [  
                  {  
                     "payload": {  
                        "url": "https://cdn.fbsbx.com/v/t59.3654-21/15308171_1226846694027684_8966586941638180864_n.flac/brooklyn.flac?_nc_cat=101&_nc_ht=cdn.fbsbx.com&oh=c199b6ff6a69fa6c4c8e39984ad0d55c&oe=5C51ABEA"
                     },
                     "type": "audio"
                  }
               ],
               "mid": "5SzQcLdjmKm8yUMzvRqhyaIP7U1RzGN2MLu2WlPcaUX06tqyMGXcdh3ENeLI34GNULqe6TLAZgMZ2EgDusY-Bw",
               "seq": 24799.0
            },
            "timestamp": 1548754168990.0
         },
         "source": "facebook"
      }
   },
   "session": "projects/pristine-atom-226517/agent/sessions/7128851b-8967-49f6-8f04-8a86ca97137d"
}

sample_facebook_opus_request_en = {
   "responseId": "959c96e0-7ffd-46d0-9055-13204e0c9033",
   "queryResult": {  
      "queryText": "FACEBOOK_MEDIA",
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
            "name": "projects/pristine-atom-226517/agent/sessions/f35afb09-42c4-45c1-8b49-ff7d4c066409/contexts/facebook_media"
         },
         {  
            "name": "projects/pristine-atom-226517/agent/sessions/f35afb09-42c4-45c1-8b49-ff7d4c066409/contexts/defaultfallbackintent-followup",
            "lifespanCount": 2
         },
         {  
            "name": "projects/pristine-atom-226517/agent/sessions/f35afb09-42c4-45c1-8b49-ff7d4c066409/contexts/generic",
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
               "attachments": [  
                  {  
                     "payload": {  
                        "url": "https://cdn.fbsbx.com/v/t59.2708-21/50203080_2581615095187609_8740172015438135296_n.opus/AUDIO-2019-01-29-16-59-57.opus?_nc_cat=100&_nc_ht=cdn.fbsbx.com&oh=527d943bfd5714911ded0b24f33e5c29&oe=5C529B4D"
                     },
                     "type": "file"
                  }
               ],
               "mid": "tFzHTaMzHfBDy--s4WCdMKIP7U1RzGN2MLu2WlPcaUX63eAOzkR-p9GeFXwNGKhTVsyYfbuMdI04J9x4vZ6qvQ",
               "seq": 24864.0
            },
            "timestamp": 1548781287990.0
         },
         "source": "facebook"
      }
   },
   "session": "projects/pristine-atom-226517/agent/sessions/f35afb09-42c4-45c1-8b49-ff7d4c066409"
}


sample_facebook_opus_request_it = {  
   "responseId": "4317f8d5-5fbe-41b2-a80c-020e25066114",
   "queryResult": {  
      "queryText": "FACEBOOK_MEDIA",
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
            "name": "projects/pristine-atom-226517/agent/sessions/250c2e62-5c94-49f6-a2f6-fd3d04fb78b1/contexts/facebook_media"
         },
         {  
            "name": "projects/pristine-atom-226517/agent/sessions/250c2e62-5c94-49f6-a2f6-fd3d04fb78b1/contexts/defaultfallbackintent-followup",
            "lifespanCount": 2
         },
         {  
            "name": "projects/pristine-atom-226517/agent/sessions/250c2e62-5c94-49f6-a2f6-fd3d04fb78b1/contexts/generic",
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
               "attachments": [  
                  {  
                     "payload": {  
                        "url": "https://cdn.fbsbx.com/v/t59.2708-21/51190382_597970917343490_2531532000041369600_n.opus/AUDIO-2019-01-30-08-45-16.opus?_nc_cat=111&_nc_ht=cdn.fbsbx.com&oh=d2317597f77e9076e183adcdc3fd3cfd&oe=5C54116C"
                     },
                     "type": "file"
                  }
               ],
               "mid": "xqvUYZ9i5ieyHE8KyaRtkaIP7U1RzGN2MLu2WlPcaUUL5zoyuR97GAGvfH5LC8U1J_aiG75XD38ZINAS62EESg",
               "seq": 24889.0
            },
            "timestamp": 1548837992892.0
         },
         "source": "facebook"
      }
   },
   "session": "projects/pristine-atom-226517/agent/sessions/250c2e62-5c94-49f6-a2f6-fd3d04fb78b1"
}