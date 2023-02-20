# AI-Assistant

Speech-based GPT-3 assistant, implemented using Deepgram for speech-to-text and ElevenLabs for text-to-speech.

Google Text-to-Speech (gTTS) is also supported as a faster, free, local alternative to ElevenLabs.

## To Run
Python 3.7 or higher is required.

1. Install dependencies:
```bash
pip install openai deepgram-sdk python-dotenv pydub requests gTTS
```

2. Create a `.env` file in the root directory with your API keys for [OpenAI](https://platform.openai.com/account/api-keys), [ElevenLabs](https://beta.elevenlabs.io/speech-synthesis), and [Deepgram](https://console.deepgram.com/), as well as the [ElevenLabs voice ID](https://api.elevenlabs.io/docs#/voices/Get_voices_v1_voices_get) you want to use for the assistant. Refer to [`.env.example`](/.env.example) for an example.

3. Start the assistant:
```bash
python assistant_driver.py
```

## Modifying Text-to-Speech
Google Text-to-Speech (gTTS) does not have as high-quality voices as ElevenLabs, but it is free, faster, and can run locally.
You can modify [`assistant_driver.py`](/assistant_driver.py#L2) to import the `text_to_speech` method from [`text_to_speech/google.py`](/text_to_speech/google.py) instead of [`text_to_speech/elevenlabs.py`](/text_to_speech/elevenlabs.py). For example:
```python
# from text_to_speech.elevenlabs import text_to_speech
from text_to_speech.google import text_to_speech
```

### Acknowledgements
The speech recongition implementation was modified from [@saharmor](https://github.com/saharmor/whisper-playground).
I referred to [Deepgram's documentation](https://developers.deepgram.com/sdks-tools/sdks/python-sdk/pre-recorded-transcription/) for help implementing speech-to-text.
I referred to [ElevenLabs' documentation](https://api.elevenlabs.io/docs) for help setting up text-to-speech.
I also used [ChatGPT](https://chat.openai.com) to help me generate and refactor code.
