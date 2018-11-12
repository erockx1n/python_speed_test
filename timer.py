#!/usr/bin/env python
import time


class Timer:
    """Simple timer to be used to output the time needed for execution"""
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start(self):
        """Sets and returns the start time"""
        self.start_time = time.time()
        return self.start_time

    def end(self):
        """Sets the end time and returns the diff between end and start time"""
        self.end_time = time.time()
        return self.end_time - self.start_time


def main():
    """Example usage of timer"""
    t = Timer()
    t.start()

    # Wait 2 seconds
    time.sleep(2)

    print(str(t.end()) + "s")


if __name__ == "__main__":
    main()
