# SLACK ENDPOINT CONSTANT
SLACK_API_HOST = 'slack.com'
SLACK_MANIFEST_EXPORT_API = '/api/apps.manifest.export'
SLACK_MANIFEST_UPDATE_API = '/api/apps.manifest.update'
SLACK_API_TOOLING_TOKENS_ROTATE_API = '/api/tooling.tokens.rotate'


class SlackApiEndpoint:
    def __init__(self):
        self.slack_api_host = SLACK_API_HOST
        self.slack_manifest_export_api = SLACK_MANIFEST_EXPORT_API
        self.slack_manifest_update_api = SLACK_MANIFEST_UPDATE_API
        self.slack_tooling_tokens_rotate_api = SLACK_API_TOOLING_TOKENS_ROTATE_API

    def get_slack_host(self):
        return self.slack_api_host

    def get_slack_manifest_export_api(self):
        return self.slack_manifest_export_api

    def get_slack_manifest_update_api(self):
        return self.slack_manifest_update_api

    def get_slack_tooling_tokens_rotate_api(self):
        return self.slack_tooling_tokens_rotate_api
