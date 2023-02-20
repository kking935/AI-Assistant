# Import custom modules
from text_to_speech.elevenlabs import text_to_speech
# from text_to_speech.google import text_to_speech
from text_to_text.gpt import text_to_text
from speech_to_text.deepg import speech_to_text

# Initial AI introduction
AI_INTRODUCTION = 'Hi friend! My name is Sam and I am an AI created by Open AI, with help from Deepgram, Eleven Labs, and Ken King. Is there anything I can help you with today? Feel free to ask away!'
# Initial prompt
INITIAL_PROMPT = f"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nAI: {AI_INTRODUCTION}\n"

# Audio format
FORMAT = "mp3"
# Stop word to abort transcription
STOP_WORD = "stop"
# Energy level for mic to detect
ENERGY = 500
# Minimum length of silence (sec) that will register as the end of a phrase
PAUSE = 0.8
# Flag to enable dynamic energy
DYNAMIC_ENERGY = True
# Default temp file name
TEMP_FILE = "temp.wav"

# ----------------------------------------

import io
import os
import re
from pydub import AudioSegment
from speech_recognition import Microphone, Recognizer
import tempfile

temp_dir = tempfile.mkdtemp()
save_path = os.path.join(temp_dir, TEMP_FILE)

def start_conversation():
    # Load the speech recognizer with CLI settings
    recognizer = Recognizer()
    recognizer.energy_threshold = ENERGY
    recognizer.pause_threshold = PAUSE
    recognizer.dynamic_energy_threshold = DYNAMIC_ENERGY
    
    conversation = INITIAL_PROMPT
    print(conversation)
    text_to_speech(AI_INTRODUCTION)

    with Microphone(sample_rate=16000) as source:
        while True:
            try:
                # Record the speech (and save to a file)
                audio = recognizer.listen(source)
                audio_clip = AudioSegment.from_file(io.BytesIO(audio.get_wav_data()))
                audio_clip.export(save_path, format=FORMAT)

                # Convert speech to text
                transcript = speech_to_text(save_path, FORMAT)

                # Check if there was an error with the transcription
                if transcript == "":
                    print("*** Transcription was empty, try again ***")
                    continue

                # Format text for conversation
                transcript = f"Human: {transcript}\n"
                
                # Print the transcript
                print(transcript)

                # Add the transcript to the conversation
                conversation += transcript

                # Send the conversation to GPT for a text response
                response = text_to_text(conversation)

                # Print the text response
                print(response)

                # Format the response
                response = response.replace("AI: ", "")

                # Check if there was an error with the response
                if response == "":
                    print("*** Response was empty, try again ***")
                    continue

                # Convert the text response to speech
                text_to_speech(response)
                
                # Add the text response to the conversation
                conversation += f"AI: {response}\n"

                # Check if stop word is detected
                if re.compile('[\W_]+', re.UNICODE) .sub('', transcript).lower() == STOP_WORD:
                    break
            except KeyboardInterrupt:
                # This code will run when the user presses "CTRL + C"
                # Print the conversation
                print("\n\n=============== EXITING ===============")
                print("\n----------------\n| Conversation |\n----------------\n")
                print(conversation)
                break


if __name__ == "__main__":
    start_conversation()