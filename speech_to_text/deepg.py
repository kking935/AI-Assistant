# Load the Deepgram API key from the .env file
import os
from dotenv import load_dotenv
load_dotenv()
DEEPGRAM_API_KEY = os.environ.get("DEEPGRAM_API_KEY")

# Import, initialize, and set Deepgram options
from deepgram import Deepgram
dg_client = Deepgram(DEEPGRAM_API_KEY)
options = { "punctuate": True, "model": "general", "language": "en-US", "tier": "enhanced" }

def speech_to_text(audio_path, audio_mimetype):
    with open(audio_path, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': audio_mimetype}
        response = dg_client.transcription.sync_prerecorded(source, options)
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
    return transcript.strip()

# print(speech_to_text('example.mp3', 'audio/mp3'))