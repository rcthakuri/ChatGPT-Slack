from chatgpt_slack_lib.bot import slack_chatgpt


def app():
    slack_chatgpt.SlackChatGPTBolt()


if __name__ == "__main__":
    app()
