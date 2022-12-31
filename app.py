import os
from dotenv import load_dotenv
from bot import slack_chatgpt

load_dotenv()

# SLACK KEY
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
PORT_FOR_SLACK_APP = os.environ.get("PORT_FOR_SLACK_APP")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")

# OPENAI CHATGPT KEY
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL_ENGINE = os.environ.get("OPENAI_MODEL_ENGINE")


def app():
    slack_key = {
        'PORT': PORT_FOR_SLACK_APP,
        'BOT_TOKEN': SLACK_BOT_TOKEN,
        'SIGNING_SECRET': SLACK_SIGNING_SECRET

    }

    chatgpt_key = {
        'OPENAI_API_KEY': OPENAI_API_KEY,
        'OPENAI_MODEL_ENGINE': OPENAI_MODEL_ENGINE,
    }

    slack_chatgpt.SlackChatGPTBolt(slack_key, chatgpt_key)


if __name__ == "__main__":
    app()
