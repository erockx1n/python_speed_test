#!/usr/bin/env python

from timer import Timer
from collections import deque
import matplotlib.pyplot as plt


def test_list(timer, iterations):
    """Appends twice & pops form a list for the given number  of iterations"""
    timer.start()
    a = list()
    for i in range(iterations):
        a.append(i)
        a.append(i)
        a.pop(0)
    return timer.end()


def test_deque(timer, iterations):
    """Appends twice & pops form a deque for the given number  of iterations"""
    timer.start()
    d = deque()
    for i in range(iterations):
        d.append(i)
        d.append(i)
        d.popleft()
    return timer.end()


def main():
    """Compares list and deque for a defined number of iterations"""
    timer = Timer()

    iterations = 100000

    time_list = test_list(timer, iterations)
    print(u"\u279c Regular list: {}ms".format(time_list*1000))

    time_deque = test_deque(timer, iterations)
    print(u"\u279c Deque: {}ms".format(time_deque*1000))

    print(u"\u279c Deque is {} faster than regular list for {} iterations."
          .format(time_list/time_deque, iterations))


def main_with_plot():
    """Generates a plot for altering iteration numbers."""
    timer = Timer()

    max_iterations = 100000
    iterations = []
    list_durations = []
    deque_durations = []
    for i in range(0, max_iterations, 10000):
        print("Processing {}/{}...".format(i, max_iterations))
        iterations.append(i)
        list_duration = test_list(timer, i)
        deque_duration = test_deque(timer, i)

        list_durations.append(list_duration)
        deque_durations.append(deque_duration)

    # Plotting
    figure, ax = plt.subplots(figsize=(14, 10), facecolor='w')
    ax.grid(True)
    ax.plot(iterations, list_durations, '-xb', label='list')
    ax.plot(iterations, deque_durations, '-xr', label='deque')
    ax.set_xlabel("Iterations")
    ax.set_ylabel("Time in seconds")
    ax.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    main()
    main_with_plot()
