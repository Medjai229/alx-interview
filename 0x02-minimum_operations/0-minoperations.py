#!/usr/bin/python3
"""
0-minoperations.py

This module contains the function minOperations

Provides a function to calculate the minimum number of operations to transform a number into 1.

Author: Malik Hussein
"""

def minOperations(n: int) -> int:
    """
    Calculates the minimum number of operations required
    to transform a number `n` into 1.

    Args:
        n (int): The number to transform.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 0:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
