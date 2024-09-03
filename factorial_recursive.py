#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the given integer. If n is 0, returns 1 since 0! is defined as 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
