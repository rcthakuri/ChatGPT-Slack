import os
import time
import pickle
import atexit
from dotenv import load_dotenv
from chatgpt_slack_lib.app_management.client.slack.slack_client import SlackClient

load_dotenv()

# SLACK CREDENTIAL
SLACK_PASSWORD = os.environ.get("SLACK_PASSWORD")
SLACK_USERNAME = os.environ.get("SLACK_USERNAME")

# SLACK APP MANIFEST KEY
SLACK_APP_ID = os.environ.get('SLACK_APP_ID')
SLACK_PORT = os.environ.get('PORT_FOR_SLACK_APP')
SLACK_APP_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET')
SLACK_CONFIG_REFRESH_TOKEN = os.environ.get('SLACK_CONFIG_REFRESH_TOKEN')


class SlackAuth:
    def __init__(self):
        self._app_id = SLACK_APP_ID
        self._slack_port = int(SLACK_PORT)
        self._slack_username = SLACK_USERNAME
        self._slack_password = SLACK_PASSWORD

        self._slack_config_token = None
        self._slack_config_token_expiry_time = None
        self._slack_config_token_created_time = None
        self.fetch_config_tokens_when_time_is_lt = 5  # hours
        self._slack_config_refresh_token = SLACK_CONFIG_REFRESH_TOKEN

        self._slack_app_token = SLACK_APP_TOKEN
        self._slack_signing_secret = SLACK_SIGNING_SECRET

        self._slack_client = SlackClient()

        self.slack_secrets_store_path = os.path.abspath('chatgpt_slack_lib/app_management/authentication/secret_vault')

        self.set_config_tokens_via_secret_file()
        atexit.register(self.slack_auth_cleanup)

    def get_app_id(self):
        return self._app_id

    def get_slack_port(self):
        return self._slack_port

    def get_slack_app_token(self):
        return self._slack_app_token

    def get_slack_signing_secret(self):
        return self._slack_signing_secret

    def get_slack_config_refresh_token(self):
        return self._config_bear_refresh_token

    def get_slack_credential(self):
        return {
            'username': self._slack_username,
            'password': self._slack_password,
        }

    def get_slack_config_token_pairs(self):
        return self._slack_client.get_slack_config_token_pair(self._slack_config_refresh_token)

    def set_config_tokens(self, config_token_data):
        self._slack_config_token = config_token_data['token']
        self._slack_config_token_expiry_time = config_token_data['exp']
        self._slack_config_token_created_time = config_token_data['iat']
        self._slack_config_refresh_token = config_token_data['refresh_token']

    def set_config_tokens_via_secret_file(self):
        try:
            with open(self.slack_secrets_store_path + '/slack_secret.pickle', 'rb') as slack_secrets:
                config_token_data = pickle.load(slack_secrets)
                self.set_config_tokens(config_token_data)
        except FileNotFoundError:
            pass

    def check_config_token_validity(self):
        if (self._slack_config_token_expiry_time - time.time()) / 60 / 60 \
                < self.fetch_config_tokens_when_time_is_lt:
            config_token_data = self.get_slack_config_token_pairs()
            self.set_config_tokens(config_token_data)

    def slack_auth_cleanup(self):
        with open(self.slack_secrets_store_path + '/slack_secret.pickle', 'wb') as slack_secrets:
            config_token_data = self.get_slack_config_token_pairs()
            pickle.dump(config_token_data, slack_secrets)
