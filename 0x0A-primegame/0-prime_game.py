#!/usr/bin/python3
"""A prime game program"""


def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def play_game(primes):
    """Choose prime"""
    player = 0
    while primes:
        choice = primes.pop(0)
        primes = [prime for prime in primes if prime % choice != 0]
        if len(primes) == 0:
            break
        """print(f"Choice: {choice}, new primes {primes}")"""
        player = 1 - player
    """print(f"Winner for this round {player}")"""
    return player


def isWinner(x, nums):
    """Play the prime game"""
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        """print(f"Round: {i}")"""
        primes = [j for j in range(0, nums[i] + 1) if is_prime(j)]
        """print(primes)"""

        if len(primes) == 0:
            ben_wins += 1
        else:
            if play_game(primes) == 0:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
