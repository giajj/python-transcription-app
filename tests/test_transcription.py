import io
import os

from transcription import speech_to_text


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
