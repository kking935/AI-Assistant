# Load the OpenAI API key from the .env file
import os
from dotenv import load_dotenv
load_dotenv()

# Import, initialize, and set default parameters for OpenAI SDK
import openai
openai.api_key = os.environ.get("OPENAI_API_KEY")

def speech_to_text(audio_path, audio_mimetype):
    audio_file = open(audio_path, "rb")
    transcript = openai.Audio.translate("whisper-1", audio_file)
    print(transcript)
    return transcript.text.strip()

# print(speech_to_text('example.mp3', 'audio/mp3'))
