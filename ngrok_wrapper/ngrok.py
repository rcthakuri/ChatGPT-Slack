import logging
from pyngrok import ngrok
from utility.custom_thread import CustomThread
from pyngrok.exception import PyngrokNgrokURLError, PyngrokNgrokURLError



class TunnelNg:
    def __init__(self, auth_token, port, request_type):
        self.port = port 
        self.auth_token = auth_token
        self.request_type = request_type
        ngrok.set_auth_token(self.auth_token)
        self.default_tunnel = None
        self.tunnel_runner = None
        self.tunnel_process_runner = None
        self.start_tunnel()

    def __del__(self):
        self.stop_tunnel()

    def build_tunnel_threads(self):
        self.tunnel_runner = CustomThread(self.ngrok_process)
        self.tunnel_process_runner = CustomThread(ngrok.get_ngrok_process().proc.wait)
        
    def start_tunnel(self):
        while not self.tunnel_runner\
            or not self.tunnel_process_runner:
            self.build_tunnel_threads()
        ngrok.connect(self.port, self.request_type)
        self.default_tunnel =  self.select_https_url(self.get_public_urls(ngrok.get_tunnels))
        logging.warning('Default tunnel updated: %s', self.default_tunnel) # TODO: Custom logging w/ color 
        self.tunnel_runner.start()


    def stop_tunnel(self):
        ngrok.kill()
        self.tunnel_runner.stop_it() 
        self.tunnel_process_runner.stop_it()
        self.tunnel_runner.join()
        self.tunnel_process_runner.join()

        self.tunnel_runner = None
        self.tunnel_process_runner  = None

    def ngrok_process(self):
        try:
            self.tunnel_process_runner.start()
        except KeyboardInterrupt:
            self.stop_tunnel()

    def poll_tunnels(self):
        while True:
            try:
                if self.default_tunnel  not in self.get_public_urls(ngrok.get_tunnels):
                    self.stop_tunnel()
                    self.start_tunnel()
            # TODO: Add possible exceptions and handle it
            except [ConnectionResetError, PyngrokNgrokURLError, PyngrokNgrokURLError]: 
                pass


    @staticmethod
    def get_public_urls(ngrok_get_tunnel_callback) -> list:
        return [tunnel.public_url for tunnel in ngrok_get_tunnel_callback()]

    @staticmethod
    def select_https_url(urls_list) -> str or None:
        https_url = list(filter(lambda x : x.startswith('https'), urls_list))
        return len(https_url) and https_url[0] or None