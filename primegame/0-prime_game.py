#!/usr/bin/python3
"""Prime game module."""


def isWinner(x, nums):
    """Determine who wins the most rounds of the prime game.

    Args:
        x: number of rounds.
        nums: list of n values, one per round.

    Returns:
        The name of the player with the most wins, or None if the
        winner cannot be determined (tie).
    """
    if not nums or x <= 0:
        return None

    nums = nums[:x]
    n = max(nums)
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, n + 1, i):
                sieve[multiple] = False

    prime_count = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if prime_count[num] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
