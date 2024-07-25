#!/usr/bin/python3
"""
Pascal Triangle Generator

This module generates a Pascal triangle with a specified number of rows.

Functions:
    pascal_triangle(n): Returns a list of lists of integers
    representing the Pascal triangle of n rows.
"""


def pascal_triangle(n):
    """
    Generates a Pascal triangle with n rows.

    Args:
        n (int): The number of rows in the Pascal triangle.

    Returns:
        list[list[int]]: A list of lists of integers
        representing the Pascal triangle.
    """
    result = []
    if n <= 0:
        return result
    for i in range(n):  # iterate over the rows of the Pascal triangle
        row = []
        prev = 1  # temp variable
        for j in range(i + 1):  # calculate the current element based on temp
            if j == 0 or j == i:  # the first and last elements are always 1
                row.append(1)
            else:
                curr = prev * (i - j + 1) // j
                row.append(curr)
                prev = curr  # store the current valuefor the next element
        result.append(row)
    return result
