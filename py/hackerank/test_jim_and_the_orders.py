# https://www.hackerrank.com/challenges/jim-and-the-orders
import heapq
from typing import List


def jim_and_the_orders(orders: List) -> List[int]:
    data = [(op[0] + op[1], uid) for uid, op in enumerate(orders, 1)]
    heapq.heapify(data)
    return [heapq.heappop(data)[1] for _ in range(len(data))]


def test_jim_and_the_orders():
    assert jim_and_the_orders([(1, 3), (2, 3), (3, 3)]) == [1, 2, 3]
