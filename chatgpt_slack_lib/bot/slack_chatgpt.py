from sys import exit
from slack_bolt import App
from slack_sdk import WebClient
from chatgpt_slack_lib.chatgpt_wrapper import chatgpt
from chatgpt_slack_lib.utility.custom_thread import CustomThread
from chatgpt_slack_lib.app_management.authentication.slack_auth import SlackAuth
from chatgpt_slack_lib.app_management.authentication.chatgpt_auth import ChatGPTAuth


class SlackChatGPTBolt(SlackAuth, ChatGPTAuth):
    def __init__(self):
        SlackAuth.__init__(self)
        ChatGPTAuth.__init__(self)
        self.replier = chatgpt.ChatGPT(self._chatgpt_model_engine, self._chatgpt_api_key)
        self.app = self.setup_app(self._slack_app_token, self._slack_signing_secret)
        self.app.start()

    def setup_app(self, bot_token, signing_secret):
        if bot_token and signing_secret:
            app = App(
                token=bot_token,
                signing_secret=signing_secret
            )
            replier = self.replier

            @app.event("app_mention")
            def handle_mention(ack, event):
                ack()
                channel = event["channel"]
                user_question = event["text"]
                reply = replier.ask(user_question)
                slack_client = WebClient(token=bot_token)
                slack_client.chat_postMessage(channel=channel, text=reply)

            return app
        else:
            print('Unable to init app!')
            exit(-1)
