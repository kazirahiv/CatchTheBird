import time
from threading import Thread


class TimerThread(Thread):
    def __init__(self, end_game):
        self.end_game = end_game
        self.counter = 5
        Thread.__init__(self, daemon=True)

    def run(self):
        while self.counter:
            time.sleep(1)
            self.counter -= 1
        self.end_game()

    def reset(self):
        self.counter = 5

    def won(self):
        self.counter = 10000
