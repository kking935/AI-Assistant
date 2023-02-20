# Set the audio path and format
audio_path = "audio.mp3"
audio_format = "mp3"


# Default temp file name
TEMP_FILE = "temp.wav"

import os
import tempfile
temp_dir = tempfile.mkdtemp()
save_path = os.path.join(temp_dir, TEMP_FILE)


# Import the audio playback library
from pydub import AudioSegment
from pydub.playback import play

# -----------------------------------------------

# Import the Google text to speech library
from gtts import gTTS

def text_to_speech(text):
    tts = gTTS(text)
    tts.save(audio_path)
    audio = AudioSegment.from_file(audio_path, format=audio_format)
    play(audio)

# text_to_speech("Hello, world!")