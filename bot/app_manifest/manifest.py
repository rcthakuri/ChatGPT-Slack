import json
from utility.http_client import HttpClient


class SlackAppManifest:
    def __init__(self, slack_key):
        self.app_id = slack_key['APP_ID']
        self.slack_app_bearer_token = slack_key['APP_BEAR_TOKEN']
        self.slack_api_connection = HttpClient(slack_key['API_HOST'])
        self.slack_manifest_export_api = slack_key['MANIFEST_EXPORT_API']
        self.slack_manifest_update_api = slack_key['MANIFEST_UPDATE_API']
        self.headers = self.get_headers(slack_key['CONFIG_BEAR_TOKEN'], 'application/json')
        self.current_app_manifest = self.get_current_app_manifest()

    def get_current_app_manifest(self):
        payload = json.dumps({
            "app_id": self.app_id
        })
        response = self.slack_api_connection.post(self.slack_manifest_export_api, payload, self.headers)
        data = response.read()
        manifest = json.loads(data.decode("utf-8"))["manifest"]
        return manifest

    def set_app_manifest(self, manifest):
        payload = json.dumps({
            'manifest': manifest,
            'app_id': self.app_id
        })
        response = self.slack_api_connection.post(self.slack_manifest_update_api, payload, self.headers)
        return response.read()

    def update_request_url(self, req_url):
        self.current_app_manifest['settings']['event_subscriptions']['request_url'] = req_url + '/slack/events'
        self.set_app_manifest(self.current_app_manifest)

    @staticmethod
    def get_headers(bearer_token, content_type):
        return {
            'Authorization': 'Bearer ' + bearer_token,
            'Content-Type': content_type
        }
