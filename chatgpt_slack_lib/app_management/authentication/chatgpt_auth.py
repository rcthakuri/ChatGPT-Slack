import os
from dotenv import load_dotenv

load_dotenv()

# OPENAI CHATGPT KEY
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL_ENGINE = os.environ.get("OPENAI_MODEL_ENGINE")


class ChatGPTAuth:
    def __init__(self):
        self._chatgpt_api_key = OPENAI_API_KEY
        self._chatgpt_model_engine = OPENAI_MODEL_ENGINE

    def get_chatgpt_api_key(self):
        return self._chatgpt_api_key

    def get_chatgpt_model_engine(self):
        return self._chatgpt_model_engine
