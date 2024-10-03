#!/usr/bin/python3
"""
Module to solve the prime game problem.
"""


def sieve_of_eratosthenes(n):
    """
    Generates prime numbers of n using the Sieve of Eratosthenes algorithm.
    """
    primes = [1] * (n + 1)

    primes[0] = primes[1] = 0

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, n + 1, i):
                primes[multiple] = 0

    return primes


def isWinner(x, nums):
    """
    Given a list of positive integers, determine the winner of the prime game.

    In prime game, the first player (Maria) wins if the count of prime numbers
    in the list is odd, and the second player (Ben) wins if the count is even.
    """
    if x <= 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    for n in nums:
        turns = sum(primes[0:n + 1])
        if turns % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
