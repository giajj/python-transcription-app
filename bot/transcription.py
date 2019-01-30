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

import os

from flask import current_app

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def speech_to_text(uri, language_code_list, sample_rate=16000):
    # Instantiates a client
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=uri)

    _, extension = os.path.splitext(uri)
    if extension == '.flac':
        encoding = enums.RecognitionConfig.AudioEncoding.FLAC
    elif extension == '.opus':
        encoding = enums.RecognitionConfig.AudioEncoding.OGG_OPUS
    else:
        return 'File extension not supported'

    confidences = []
    transcripts = []
    for language_code in language_code_list:
        config = types.RecognitionConfig(
            encoding=encoding,
            sample_rate_hertz=sample_rate,
            language_code=language_code
        )

        # Detects speech in the audio file
        response = client.recognize(config, audio)
        try:
            confidences.append(response.results[0].alternatives[0].confidence)
            transcripts.append(response.results[0].alternatives[0].transcript)
        except Exception as e:
            current_app.logger.info('Error: %s', e)

    if len(confidences) > 0:
        idx_max_conf = argmax(confidences)
        current_app.logger.info('Detected language: %s, Confidence: %.2f',
                                language_code_list[idx_max_conf], confidences[idx_max_conf])
        return transcripts[idx_max_conf]
    else:
        return 'An error occurred during the transcription'


def argmax(iterable):
    return max((x, i) for i, x in enumerate(iterable))[1]
