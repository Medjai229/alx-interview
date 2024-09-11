#!/usr/bin/python3
"""Rotates a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise
    """
    # Get the length of the matrix
    n = len(matrix)

    # Iterate over the matrix, swapping elements to rotate it
    # Start from the outside and work our way in
    for i in range(n // 2):
        # Iterate over the elements in the current ring
        for j in range(i, n - i - 1):
            # Store the top left element
            temp = matrix[i][j]

            # Assign the bottom left element to the top left element
            matrix[i][j] = matrix[n - 1 - j][i]

            # Assign the bottom right element to the bottom left element
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]

            # Assign the top right element to the bottom right element
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]

            # Assign the top right element to the stored element
            matrix[j][n - 1 - i] = temp
