import os
from dotenv import load_dotenv
from chatgpt_slack_lib.ngrok_wrapper.ngrok import TunnelNg
from chatgpt_slack_lib.app_management.app_manifest.slack_app_manifest import SlackAppManifest

load_dotenv()

# NGROK KEY
NGROK_PORT = os.environ.get('NGROK_PORT')
NGROK_AUTH_TOKEN = os.environ.get('NGROK_AUTH_TOKEN')
NGROK_REQUEST_TYPE = os.environ.get('NGROK_REQUEST_TYPE')


def updator():
    ngrok_key = {
        'PORT': NGROK_PORT,
        'AUTH_TOKEN': NGROK_AUTH_TOKEN,
        'REQUEST_TYPE': NGROK_REQUEST_TYPE
    }
    app_manifest = SlackAppManifest()
    TunnelNg(ngrok_key, app_manifest.update_request_url).poll_tunnels()
