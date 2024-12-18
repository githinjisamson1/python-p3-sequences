#!/usr/bin/env python3


def print_fibonacci(length):
    if length == 0:
        fibonacci_series = []
    elif length == 1:
        fibonacci_series = [0]
    else:
        # initialize fibonacci
        fibonacci_series=[0, 1]
        
        # as long as end is not reached
        while len(fibonacci_series) < length:
            next_number = fibonacci_series[-1] + fibonacci_series[-2]
            fibonacci_series.append(next_number)
    
    print(fibonacci_series)


