# AI-Assistant

Speech-based GPT-3 assistant, implemented using Deepgram for speech-to-text and ElevenLab for text-to-speech.

Google Text-to-Speech (gTTS) is also supported as a faster, free, local alternative to ElevenLab.

## To Run
Python 3.7 or higher is required.

1. Install dependencies:
```bash
pip install openai deepgram-sdk python-dotenv pydub requests gTTS
```

2. Create a `.env` file in the root directory with your API keys for OpenAI, ElevenLab, and Deepgram, as well as the ElevenLab voice ID you want to use for the asistant. Refer to [`.env.example`](/.env.example) for an example.

3. Start the assistant:
```bash
python driver_assistant.py
```

## Modifying Text-to-Speech
Google Text-to-Speech (gTTS) does not have as high-quality voices as ElevenLab, but it is free, faster, and can run locally.
You can modify [`driver_assistant.py`](/driver_assistant.py) to import the `text_to_speech` method from [`text_to_speech/simple.py`](/text_to_speech/simple.py) instead of [`text_to_speech/eleven.py`](/text_to_speech/eleven.py). For example:
```python
# from text_to_speech.eleven import text_to_speech
from text_to_speech.simple import text_to_speech
```

### Acknowledgements
The speech recongition implementation was modified from [@saharmor](https://github.com/saharmor/whisper-playground).
I referred to [Deepgram's documentation](https://developers.deepgram.com/sdks-tools/sdks/python-sdk/pre-recorded-transcription/) for help implementing speech-to-text.
I referred to [ElevenLabs's documentation](https://api.elevenlabs.io/docs) for help setting up text-to-speech.
I also used [ChatGPT](https://chat.openai.com) to help me generate and refactor code.
