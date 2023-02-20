# Load the OpenAI API key from the .env file
import os
from dotenv import load_dotenv
load_dotenv()

# Import, initialize, and set default parameters for OpenAI SDK
import openai
openai.api_key = os.environ.get("OPENAI_API_KEY")
MODEL = "text-davinci-003"
MAX_TOKENS = 100
TEMPERATURE = 0

def text_to_text(conversation):
    response_data = openai.Completion.create(
        prompt=conversation,
        model=MODEL,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
    )
    response_message = response_data.choices[0].text.strip()
    return response_message.strip()

# print(text_to_text("Hello, how are you?"))