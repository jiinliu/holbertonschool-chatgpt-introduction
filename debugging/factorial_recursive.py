#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.
    
    Parameters:
        n (int): The non-negative integer for which to calculate the factorial
    
    Returns:
        int: The factorial of n (n!)
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
