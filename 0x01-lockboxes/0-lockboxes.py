#!/usr/bin/python3
"""
0-lockboxes.py

solving the "Unlock All Boxes" problem.

This module provides a function to determine if it is possible to unlock
all boxes given the keys in each box.

Author: Malik Hussein
"""


def canUnlockAll(boxes):
    """
    Determines if it is possible to unlock all boxes
    given the keys in each box.

    Args:
        boxes (list of lists): A list of boxes
        where each box is a list of keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.

    Example:
        >>> boxes = [[1], [2], [3], [4], []]
        >>> canUnlockAll(boxes)
        True
        >>> boxes = [[1, 4], [2], [3], [], [5]]
        >>> canUnlockAll(boxes)
        False
    """
    n = len(boxes)
    opened = set()
    stack = [0]

    while stack:
        box = stack.pop()
        if box not in opened:
            opened.add(box)
            for key in boxes[box]:
                if key < n and key not in opened:
                    stack.append(key)

    return len(opened) == n
