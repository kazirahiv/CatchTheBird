import time
from threading import Thread


class MoveBirdThread(Thread):
    def __init__(self, callback, level_up):
        self.terminated = False
        self.callback = callback
        self.level_up = level_up
        Thread.__init__(self, daemon=True)

    def run(self):
        while True:
            time.sleep(0.7)
            try:
                try:
                    self.callback()
                except:
                    self.level_up()
            except:
                pass