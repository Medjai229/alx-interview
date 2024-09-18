#!/usr/bin/python3
"""
Making Change module
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins that you need to make change for total
    with the coins. If total is 0, or if you can't make change, returns -1
    """
    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1

    if total == 0:
        return num_coins
    else:
        return -1
