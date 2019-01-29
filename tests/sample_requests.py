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

sample_facebook_media_request = {
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
