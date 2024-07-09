#!/usr/bin/python3
"""
0-minoperations module
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.

    :param n: int, number of H characters desired
    :return: int, minimum number of operations,
    or 0 if n is impossible to achieve
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
