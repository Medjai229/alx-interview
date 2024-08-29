#!/usr/bin/python3
"""
File: 0-nqueens.py

The N queens puzzle is the problem of placing N queens on an NxN chessboard
such that no two queens attack each other. A solution requires that
no two queens share the same row, column, or diagonal.

Author: Malik Hussein
"""
import sys


def print_usage_and_exit():
    """
    Prints the usage string and exits with status 1.
    """
    print("Usage: nqueens N")
    sys.exit(1)


def print_number_error_and_exit():
    """
    Prints an error message and exits with status 1 when N is not a number.
    """
    print("N must be a number")
    sys.exit(1)


def print_size_error_and_exit():
    """
    Prints an error message and exits with status 1 when N is less than 4.
    """
    print("N must be at least 4")
    sys.exit(1)


def is_valid(board, row, col):
    """
    Checks if a given position is valid for a queen in the board.

    The position is valid if there is no other queen in the same row,
    column or diagonal.

    Returns:
    bool: True if the position is valid, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row=0, board=[]):
    """
    Solve the N queens problem.

    The function uses a backtracking algorithm to solve the problem.
    """
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_valid(board, row, col):
            board.append(col)
            solve_nqueens(n, row + 1, board)
            board.pop()


def main():
    """
    The main function
    """
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_number_error_and_exit()

    if n < 4:
        print_size_error_and_exit()

    solve_nqueens(n)


if __name__ == "__main__":
    main()
