import http.client


class HttpClient:
    def __init__(self, host):
        self.connection = http.client.HTTPSConnection(host)

    def post(self, end_point, payload, headers=None):
        self.connection.request("POST", end_point, payload, headers)
        response = self.connection.getresponse()
        return response

    def get(self, end_point, params='', headers=None):
        self.connection.request("GET", end_point, params, headers)
        response = self.connection.getresponse()
        return response
