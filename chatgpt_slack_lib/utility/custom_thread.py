import threading


class CustomThread(threading.Thread):
    def __init__(self, target):
        super().__init__()
        self.target = target
        self._stopper = threading.Event()

    def run(self):
        self.target()
        while True:
            if self.stopped():
                return

    def stop_it(self):
        self._stopper.set()

    def stopped(self):
        return self._stopper.is_set()
