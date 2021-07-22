# -*- coding: utf-8 -*-
import threading
import time


class ThreadA(threading.Thread):

    def __init__(self, name: str, e: threading.Event):
        super().__init__(name=name)
        self.event = e

    def run(self):
        while self.event.isSet():
            print("{} {}".format(self.name, time.time()))
            time.sleep(1)
        else:
            print("event {}".format(self.event.is_set()))


def main():
    e = threading.Event()
    e.set()
    print("set event to {}".format(e.is_set()))
    for x in range(10):
        s = ThreadA("Thread {}".format(x), e)
        s.start()
    try:
        while True:
            time.sleep(1)
            print("{} {}".format("Main", time.time()))
    except KeyboardInterrupt:
        e.clear()
        print("set event to {}".format(e.is_set()))


if __name__ == '__main__':
    main()
