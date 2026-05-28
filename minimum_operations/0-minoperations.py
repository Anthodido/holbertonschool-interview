#!/usr/bin/env python3

"""method that calculates the fewest number of operations needed to result"""


def minOperations(n):
    if n is None or n <= 1:
        return 0
    operations = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n //= i
    return operations
