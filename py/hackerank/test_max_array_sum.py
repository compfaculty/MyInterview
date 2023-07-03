from typing import List


# Given an array of integers, find the subset of non-adjacent elements with the maximum sum.
# Calculate the sum of that subset. It is possible that the maximum sum is 0, the case when all elements are negative.

def max_array_sum(arr: List[int]) -> int:
    dp = {0: arr[0], 1: max(arr[0], arr[1])}
    for i, num in enumerate(arr[2:], start=2):
        dp[i] = max(dp[i - 1], dp[i - 2], dp[i - 2] + num, num)
    return dp[len(arr) - 1]


def test_max_array_sum():
    assert max_array_sum([-2, 1, 3, -4, 5]) == 8
    assert max_array_sum([-2, -1, -3, -4, -5]) == -1
    # assert max_array_sum([0]) == 0
