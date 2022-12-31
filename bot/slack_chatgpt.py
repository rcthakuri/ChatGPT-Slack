import os
import threading
from slack_bolt import App
from slack_sdk import WebClient
from chatgpt_wrapper import chatgpt


class AppRunner(threading.Thread):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self._stop = threading.Event()

    def run(self):
        self.target()
        while True:
            if self.stopped():
                return

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()


class SlackChatGPTBolt:
    def __init__(self, slack_key, chatgpt_key):
        self.replier = chatgpt.ChatGPT(chatgpt_key['OPENAI_MODEL_ENGINE'], chatgpt_key['OPENAI_API_KEY'])
        self.app = self.setup_app(slack_key['BOT_TOKEN'], slack_key['SIGNING_SECRET'])
        self.app_runner = AppRunner(self.app.start(port=int(slack_key['PORT'])))

    def __del__(self):
        self.app_runner.stop()
        exit(-1)

    def setup_app(self, bot_token, signing_secret):
        if bot_token and signing_secret:
            app = App(
                token=bot_token,
                signing_secret=signing_secret
            )
            replier = self.replier
            @app.event("app_mention")
            def handle_mention(ack, respond, logger, event):
                ack()
                user_question = event["text"]
                reply = replier.ask(user_question)
                channel = event["channel"]
                slack_client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
                slack_client.chat_postMessage(channel=channel, text=reply)
            return app
        else:
            print('Unable to init app!')
            exit(-1)

    def init_app(self):
        self.app_runner.start()
        self.app_runner.join()
