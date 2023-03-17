# SPEECH_TO_TEXT
# --------------------------------------------------------------
import os
from dotenv import load_dotenv
load_dotenv()
import openai
openai.api_key = os.environ.get("OPENAI_API_KEY")

def speech_to_text(audio_path, audio_mimetype):
    audio_file = open(audio_path, "rb")
    transcript = openai.Audio.translate("whisper-1", audio_file, language='Es')
    # print(transcript)
    return transcript.text.strip()

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

# DETECT_VOICE
# --------------------------------------------------------------
# Import custom modules
# Set the audio path and format
audio_path = "audio.mp3"
audio_format = "mp3"

# Default temp file name
TEMP_FILE = "temp.wav"

import os
import tempfile
temp_dir = tempfile.mkdtemp()
save_path = os.path.join(temp_dir, TEMP_FILE)

# Audio format
FORMAT = "mp3"
# Stop word to abort translation
STOP_WORD = "stop"
# Energy level for mic to detect
ENERGY = 500
# Minimum length of silence (sec) that will register as the end of a phrase
PAUSE = 0.8
# Flag to enable dynamic energy
DYNAMIC_ENERGY = True
# Default temp file name
TEMP_FILE = "temp.wav"

import io
import os
from speech_recognition import Microphone, Recognizer
import tempfile

temp_dir = tempfile.mkdtemp()
save_path = os.path.join(temp_dir, TEMP_FILE)

def start_conversation():
    recognizer = Recognizer()
    recognizer.energy_threshold = ENERGY
    recognizer.pause_threshold = PAUSE
    recognizer.dynamic_energy_threshold = DYNAMIC_ENERGY
    
    conversation = ''

    with Microphone(sample_rate=16000) as source:
        print("Ready.")
        while True:
            try:
                # Record the speech (and save to a file)
                audio = recognizer.listen(source)
                audio_clip = AudioSegment.from_file(io.BytesIO(audio.get_wav_data()))
                audio_clip.export(save_path, format=FORMAT)


                # Convert speech to text
                translation = speech_to_text(save_path, FORMAT)

                # Check if there was an error with the translation
                if translation == "":
                    print("*** translation was empty, try again ***")
                    continue

                # Print the translation
                print(translation)

                # Add the translation to the conversation
                conversation += translation

                # Convert the text response to speech
                text_to_speech(translation)
                
            except KeyboardInterrupt:
                # This code will run when the user presses "CTRL + C"
                # Print the conversation
                print("\n\n=============== EXITING ===============")
                print("\n----------------\n| Conversation |\n----------------\n")
                print(conversation)
                break


if __name__ == "__main__":
    start_conversation()