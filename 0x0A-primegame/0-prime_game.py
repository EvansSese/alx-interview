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


def play_game(n):
    """Start the game"""
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    player = 0  # 0 for Maria, 1 for Ben
    while primes:
        prime_choice = primes.pop(0)
        primes = [num for num in primes if num % prime_choice != 0]
        player = 1 - player
    return player


def isWinner(x, nums):
    """Determine the winner"""
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == 0:
            maria_wins += 1
        elif winner == 1:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
