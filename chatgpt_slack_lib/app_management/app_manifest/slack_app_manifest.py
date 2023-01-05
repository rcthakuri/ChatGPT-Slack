from chatgpt_slack_lib.utility.custom_thread import CustomThread
from chatgpt_slack_lib.app_management.authentication.slack_auth import SlackAuth


class SlackAppManifest(SlackAuth):
    def __init__(self):
        SlackAuth.__init__(self)
        self.slack_client = self._slack_client
        self.current_app_manifest = self.get_current_app_manifest()
        self.slack_config_token_poll_runner = CustomThread(self.poll_slack_config_token)

    def slack_manifest_cleanup(self):
        hasattr(self, 'slack_config_token_poll_runner') and \
            hasattr(self.slack_config_token_poll_runner, 'stop') and \
            self.slack_config_token_poll_runner.stop()

    def get_current_app_manifest(self):
        manifest = self.slack_client.get_slack_app_manifest(self._slack_config_token, self._app_id)
        return manifest

    def set_app_manifest(self, manifest):
        response = self.slack_client.set_slack_app_manifest(self._slack_config_token, self._app_id, manifest)
        return response

    def update_request_url(self, req_url):
        self.current_app_manifest['settings']['event_subscriptions']['request_url'] = req_url + '/slack/events'
        self.set_app_manifest(self.current_app_manifest)

    def poll_slack_config_token(self):
        while True:
            try:
                self.check_config_token_validity()
            except KeyboardInterrupt:
                break
