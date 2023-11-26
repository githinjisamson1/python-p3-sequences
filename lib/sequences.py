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

        while len(fibonacciSeries) < length:
            # nextNumber is as result of adding lastTwoNumbers
            nextNumber = fibonacciSeries[-1] + fibonacciSeries[-2]

            # add to list
            fibonacciSeries.append(nextNumber)

    print(fibonacciSeries)


# print_fibonacci(9)
