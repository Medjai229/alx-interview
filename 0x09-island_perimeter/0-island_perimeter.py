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
    perimeter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j]:
                # Start with 4 for each land cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
