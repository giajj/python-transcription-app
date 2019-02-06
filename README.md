# python-transcription-app

Conversational Transcription App hosted in Google App Engine. It uses Flask, Dialogflow and Facebook Messenger for 
conversational experience, Google Cloud buckets and CloudSQL for storage and Google Cloud Speech for audio 
transcription.

This App was developed using the repository 
[GoogleCloudPlatform/getting-started-python](https://github.com/GoogleCloudPlatform/getting-started-python) 
as a starting point and reference working example.

## Architecture
The App is structured as follows:

- This repository uses Flask to create an HTTP POST end-point which can handle json requests formatted as Facebook 
Messages according to [Dialogflow API V2](https://dialogflow.com/docs/reference/agent).
- This end-point app is meant to be deployed using Google App Engine
- A Dialogflow instance with active integration to Facebook Messenger handles the conversational experience and intents, 
and is configured with a Default Fallback Intent to point to the Webhook corresponding to the end-point app


## Setup
Create the necessary accounts and resources, then create a *config.yaml* file, copying from *config.yaml.dist* and 
filling the credentials required.

## Licensing

* See [LICENSE](LICENSE)
