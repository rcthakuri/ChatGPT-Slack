import json
from chatgpt_slack_lib.utility.http_client import HttpClient
from chatgpt_slack_lib.app_management.client.slack.endpoint.slack_endpoint import SlackApiEndpoint


class SlackClient(SlackApiEndpoint):
    def __init__(self):
        super().__init__()
        self.client = HttpClient(self.slack_api_host)

    def get_slack_config_token_pair(self, refresh_token):
        response = self.client.get(self.slack_tooling_tokens_rotate_api + '?refresh_token=' + refresh_token, '', {})
        data = response.read()
        config_tokens_data = json.loads(data)
        return config_tokens_data

    def get_slack_app_manifest(self, bearer_token, app_id):
        headers = self.get_headers(bearer_token, 'application/json')
        payload = json.dumps({
            "app_id": app_id
        })
        response = self.client.post(self.slack_manifest_export_api, payload, headers)
        data = response.read()
        manifest = json.loads(data.decode("utf-8"))["manifest"]
        return manifest

    def set_slack_app_manifest(self, bearer_token, app_id, manifest):
        headers = self.get_headers(bearer_token, 'application/json')
        payload = json.dumps({
            'manifest': manifest,
            'app_id': app_id
        })
        response = self.client.post(self.slack_manifest_update_api, payload, headers)
        return response.read()

    @staticmethod
    def get_headers(bearer_token, content_type):
        return {
            'Authorization': 'Bearer ' + bearer_token,
            'Content-Type': content_type
        }
