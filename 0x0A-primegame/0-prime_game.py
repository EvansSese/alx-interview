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

    maria = 0
    ben = 0

    for i in range(x):
        """print(f"Round: {i}")"""
        maria_wins = False
        ben_wins = False
        primes = [j for j in range(0, nums[i] + 1) if is_prime(j)]
        """print(primes)"""

        if len(primes) == 0:
            ben_wins = True
            maria_wins = False
        else:
            if play_game(primes) == 0:
                maria_wins = True
                ben_wins = False
            else:
                maria_wins = False
                ben_wins = True
        if ben_wins:
            ben += 1
        if maria_wins:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
