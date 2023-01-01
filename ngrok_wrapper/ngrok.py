import threading
from pyngrok import ngrok


class TunnelNg:
    def __init__(self, auth_token, port, request_type):
        self.port = port 
        self.auth_token = auth_token
        self.request_type = request_type
        ngrok.set_auth_token(self.auth_token)
        self.tunnel_runner = AppRunner(self.ngrok_process)

    def __del__(self):
        self.stop_tunnel()

    def connect(self):
        #self.tunnel_runner.join()
        ngrok.connect(self.port, self.request_type)
        self.start_tunnel()
        return ngrok.get_tunnels()[1].public_url

    def start_tunnel(self):
        self.tunnel_runner.start()

    def stop_tunnel(self):
        self.tunnel_runner.stop()
        self.tunnel_runner.join()

    def ngrok_process(self):
        process_runner = AppRunner(ngrok.get_ngrok_process().proc.wait)
        try:
            process_runner.start()
        except KeyboardInterrupt:
            ngrok.kill()
            process_runner.join()
            process_runner.stop()
            self.tunnel_runner.stop()



class AppRunner(threading.Thread):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self._stop = threading.Event()

    def run(self):
        self.target()
        while True:
            print('run')
            if self.stopped():
                return

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.is_set()

check = TunnelNg('2JiTOdikcjiu8PfbBz07obIgx4a_4DAVcpvzBUQ3eRmryfB23',40,"http")
print(check.connect())