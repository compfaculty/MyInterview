# https://www.hackerrank.com/challenges/mark-and-toys
import heapq
from typing import List


def mark_and_toys(prices: List, k: int) -> int:
    heapq.heapify(prices)
    count = 0
    while k > 0:
        p = heapq.heappop(prices)
        k = k - p
        if k <= 0:
            break
        count += 1
    return count


def test_count_triplets_1():
    assert mark_and_toys([1, 2, 3, 4], 7) == 3
    # assert mark_and_toys([1, 2, 2], 2) == 0
    # assert mark_and_toys([], 0) == 0
    # assert mark_and_toys([], 10) == 0
    # assert mark_and_toys([], -10) == 0
