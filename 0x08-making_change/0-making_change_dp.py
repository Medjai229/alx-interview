#!/usr/bin/python3
"""
Making Change module
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins that you need to make change for total
    with the coins. If total is 0, or if you can't make change, returns -1
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
