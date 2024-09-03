#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer iteratively.

    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the given integer. The factorial of a number n is 
         the product of all positive integers less than or equal to n. 
         If n is 0 or 1, returns 1 as 0! and 1! are both defined as 1.
    """
    result = 1
    while n > 1:
        result *= n  # Multiply result by n
        n -= 1  # Decrement n by 1 in each iteration
    return result

# Get the first argument from the command line, convert it to an integer, and calculate the factorial
f = factorial(int(sys.argv[1]))
# Print the calculated factorial
print(f)
