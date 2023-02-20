# Set the audio path and format
audio_path = "audio.mp3"
audio_format = "mp3"

# Import the audio playback library
from pydub import AudioSegment
from pydub.playback import play

# -----------------------------------------------

# Load the Eleven Lab API key from the .env file
import os
from dotenv import load_dotenv
load_dotenv()
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

# Load the Eleven Lab voice ID from the .env file
VOICE_ID = os.environ.get("ELEVENLABS_VOICE_ID")

# Import requests to make HTTP requests
import requests

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

data = {
    "text": 'This is some default text',
    "voice_settings": {
        "stability": 0,
        "similarity_boost": 0
    }
}

headers = {
    "Content-Type": "application/json",
    "xi-api-key": ELEVENLABS_API_KEY
}

def text_to_speech(text):
    data["text"] = text
    response = requests.post(url, headers=headers, json=data)

    if response.ok:
        audio_data = response.content
        with open(audio_path, "wb") as f:
            f.write(audio_data)

        audio = AudioSegment.from_file(audio_path, format=audio_format)
        play(audio)

# text_to_speech('Hello world!')