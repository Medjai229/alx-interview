#!/usr/bin/python3
"""
Module to find the island perimeter
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.
    """
    height = len(grid)
    width = len(grid[0])
    counter = 0
    adj_counter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j]:
                counter += 1
                if i > 0 and grid[i - 1][j] == 1:
                    adj_counter += 1
                if j > 0 and grid[i][j - 1] == 1:
                    adj_counter += 1

    perimeter = counter * 4 - adj_counter * 2
    return perimeter
