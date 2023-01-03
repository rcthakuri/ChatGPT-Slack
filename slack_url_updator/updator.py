import os
from dotenv import load_dotenv
from ngrok_wrapper.ngrok import TunnelNg
from bot.app_manifest.manifest import SlackAppManifest

load_dotenv()

# SLACK CREDENTIAL 
SLACK_PASSWORD = os.environ.get("SLACK_PASSWORD")
SLACK_USERNAME = os.environ.get("SLACK_USERNAME")

# SLACK APP MANIFEST KEY
SLACK_APP_ID = os.environ.get('SLACK_APP_ID')
SLACK_API_HOST = os.environ.get('SLACK_API_HOST')
SLACK_APP_BEAR_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_CONFIG_BEAR_TOKEN = os.environ.get('SLACK_CONFIG_BEAR_TOKEN')
SLACK_MANIFEST_UPDATE_API = os.environ.get('SLACK_MANIFEST_UPDATE_API')
SLACK_MANIFEST_EXPORT_API = os.environ.get('SLACK_MANIFEST_EXPORT_API')

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

    slack_manifest_key = {
        'APP_ID': SLACK_APP_ID,
        'API_HOST': SLACK_API_HOST,
        'APP_BEAR_TOKEN': SLACK_APP_BEAR_TOKEN,
        'CONFIG_BEAR_TOKEN': SLACK_CONFIG_BEAR_TOKEN,
        'MANIFEST_EXPORT_API': SLACK_MANIFEST_EXPORT_API,
        'MANIFEST_UPDATE_API': SLACK_MANIFEST_UPDATE_API,
    }

    app_manifest = SlackAppManifest(slack_manifest_key)
    TunnelNg(ngrok_key, app_manifest.update_request_url).poll_tunnels()


if __name__ == "__main__":
    updator()
