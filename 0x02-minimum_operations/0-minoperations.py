#!/usr/bin/python3
"""Function to return number of minimum operations"""


def minOperations(n):
    """Finding minimum operations"""
    if n > 1:
        dp = [float('inf')] * (n + 1)
        dp[1] = 0

        for i in range(2, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
                    dp[i] = min(dp[i], dp[i // j] + j)

        return dp[n]

    return 0


if __name__ == "__main__":
    minOperations(9)

