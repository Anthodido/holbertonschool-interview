#!/usr/bin/env python3

"""method that calculates the fewest number of operations needed to result"""


def minOperations(n):
    """return the min number of operations
    Args:
        n (int): target number H
    Returns:
            int: min number
    """
    if n <= 1:
        return 0

    operations = 0
    current_length = 1

    while current_length < n:
        if n % current_length == 0:
            operations += 1
            current_length *= 2
        else:
            operations += 1
            current_length += 1

    return operations
