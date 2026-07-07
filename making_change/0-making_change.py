#!/usr/bin/python3
"""
0-making_change module
"""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins needed to make change for a given total.

    Args:
        coins (list of int): The denominations of the coins available.
        total (int): The total amount for which change is to be made.

    Returns:
        int: The minimum number of coins needed to make change, or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    dp = [0] + [float('inf')] * total

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount and dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    return dp[total] if dp[total] != float('inf') else -1
