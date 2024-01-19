#!/usr/bin/python3
"""Function to return number of minimum operations"""


def minOperations(n):
    """Finding minimum operations"""
    if not isinstance(n, int):
        return 0

    operations = 0
    iterator = 2
    while iterator <= n:
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations


if __name__ == "__main__":
    minOperations(9)
