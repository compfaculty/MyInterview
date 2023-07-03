# https://www.hackerrank.com/challenges/count-triplets-1
from typing import List


def count_triplets_1(data: List[int], r: int) -> int:
    items = {}
    double_items = {}
    ret = 0
    data.reverse()
    for item in data:
        itemr = item * r
        if itemr in double_items:
            ret += double_items[itemr]
        if itemr in items:
            tmp = double_items[item] if item in double_items else 0
            double_items[item] = tmp + items[itemr]
        tmpi = items[item] if item in items else 0
        items[item] = tmpi + 1
    return ret


def test_count_triplets_1():
    assert count_triplets_1([1, 2, 2, 4], 2) == 2
    assert count_triplets_1([1, 2, 2], 2) == 0
    assert count_triplets_1([], 0) == 0
    assert count_triplets_1([], 10) == 0
    assert count_triplets_1([], -10) == 0
