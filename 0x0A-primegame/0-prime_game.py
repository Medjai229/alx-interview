#!/usr/bin/python3
"""
Module to solve the prime game problem.
"""


def sieve_of_eratosthenes(n):
    """
    Generates prime numbers of n using the Sieve of Eratosthenes algorithm.
    """
    primes = [True] * (n + 1)

    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, n + 1, i):
                primes[multiple] = False

    return [i for i in range(2, n + 1) if primes[i]]


def isWinner(x, nums):
    """
    Given a list of positive integers, determine the winner of the prime game.

    In prime game, the first player (Maria) wins if the count of prime numbers
    in the list is odd, and the second player (Ben) wins if the count is even.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        available_nums = [True] * (n + 1)
        available_nums[0] = available_nums[1] = False
        prime_count = 0

        for prime in primes:
            if prime > n:
                break
            if available_nums[prime]:
                prime_count += 1

                for multiple in range(prime, n + 1, prime):
                    available_nums[multiple] = False

        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif maria_wins < ben_wins:
        return 'Ben'
    else:
        return None
