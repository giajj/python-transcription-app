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
import os

from bot.transcription import speech_to_text


def test_en_transcription():
    # The name of the audio file to transcribe
    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources',
        'brooklyn.flac'
    )

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        transcript = speech_to_text(content)

    assert transcript == "how old is the Brooklyn Bridge"


def test_it_transcription():
    # The name of the audio file to transcribe
    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources',
        'vpnjs-bjtf9.flac'
    )

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        transcript = speech_to_text(
            content,
            language_code='it-IT',
            sample_rate=48000,
            encoding_type='flac'
        )

    assert "Ciao Giacomino non era con me non so con chi" in transcript
