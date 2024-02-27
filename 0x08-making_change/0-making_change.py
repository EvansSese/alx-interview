#!/usr/bin/python3
"""How many coins make the change"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        if coin > total:
            continue
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
