#!/usr/bin/env python3


def print_fibonacci(length):

    if length == 0:
        fibonacciSeries = []

    elif length == 1:
        fibonacciSeries = [0]

    elif length == 2:
        fibonacciSeries = [0, 1]

    else:
        # initialize fibonacciSeries with [0, 1]
        fibonacciSeries = [0, 1]

        # execute as long as end has not been reached
        while len(fibonacciSeries) < length:
            # nextNumber is as result of adding lastTwoNumbers
            nextNumber = fibonacciSeries[-1] + fibonacciSeries[-2]

            # add to end of list
            fibonacciSeries.append(nextNumber)

    print(fibonacciSeries)


# print_fibonacci(9)
