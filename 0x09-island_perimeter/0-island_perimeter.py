#!/usr/bin/python3
"""
Module to find the island perimeter
"""


def dfs(grid, i, j):
    """
    Perform DFS to calculate the perimeter of the island.
    """
    # If the current cell is out of bounds or water
    if (i < 0 or 
    i >= len(grid) or
    j < 0 or
    j >= len(grid[0]) or
    grid[i][j] == 0):
        return 1

    # If the cell is visited before return 0
    if grid[i][j] == -1:
        return 0

    # Mark the visited cell
    grid[i][j] = -1

    # Start the perimeter
    perimeter = 0

    # Explore the neighboring cells
    perimeter += dfs(grid, i - 1, j)  # UP
    perimeter += dfs(grid, i + 1, j)  # DOWN
    perimeter += dfs(grid, i, j - 1)  # LEFT
    perimeter += dfs(grid, i, j + 1)  # RIGHT

    return perimeter


def island_perimeter(grid):
    """
    Calculates the perimeter of the island using DFS.
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # Start DFS from the first land cell
                return dfs(grid, i, j)

    # If no land was found
    return 0
