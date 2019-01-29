from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def speech_to_text(uri, encoding_type='flac', sample_rate=16000, language_code='en-US'):
    # Instantiates a client
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=uri)

    if encoding_type == 'flac':
        encoding = enums.RecognitionConfig.AudioEncoding.FLAC
    elif encoding_type == 'linear16':
        encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    elif encoding_type == 'ogg_opus':
        encoding = enums.RecognitionConfig.AudioEncoding.OGG_OPUS
    else:
        encoding = enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED

    config = types.RecognitionConfig(
        encoding=encoding,
        sample_rate_hertz=sample_rate,
        language_code=language_code
    )

    try:
        # Detects speech in the audio file
        response = client.recognize(config, audio)
        transcript = response.results[0].alternatives[0].transcript
    except Exception as e:
        transcript = 'Error: %s' % e

    return transcript
