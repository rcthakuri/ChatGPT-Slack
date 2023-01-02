import os
from dotenv import load_dotenv
from ngrok_wrapper.ngrok import TunnelNg
from automation_model.automation.automate_slack_event_subscription import SlackUrlUpdater


load_dotenv()

# SLACK CREDENTIAL 
SLACK_PASSWORD = os.environ.get("SLACK_PASSWORD")
SLACK_USERNAME = os.environ.get("SLACK_USERNAME")

# NGROK KEY
NGROK_PORT = os.environ.get('NGROK_PORT')
NGROK_AUTH_TOKEN = os.environ.get('NGROK_AUTH_TOKEN')
NGROK_REQUEST_TYPE = os.environ.get('NGROK_REQUEST_TYPE')

def updator():
    slack_cred = {
        'USERNAME': SLACK_USERNAME,
        'PASSWORD': SLACK_PASSWORD,
    }

    ngrok_key = {
        'PORT': NGROK_PORT,
        'AUTH_TOKEN': NGROK_AUTH_TOKEN,
        'REQUEST_TYPE': NGROK_REQUEST_TYPE
    }

    slack_url_updator = SlackUrlUpdater(slack_cred)
    TunnelNg(ngrok_key, slack_url_updator.update_request_url).poll_tunnels()

    
if __name__ == "__main__":
    updator()
