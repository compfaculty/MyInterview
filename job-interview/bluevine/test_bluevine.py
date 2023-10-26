from typing import List



# Write a Python function that gets a string value as input,
# and return a string that contains all chars with maximum appearances (char should be printed once).
#  For Example: s1 = "gcccggd" -> res_s = "gc"
#
def maximum_appearances(s: str) -> str:
#
# class Bluevine:
#     def task(self, nums: List[int]) -> List[int]:
#       return nums
#
#
# def test_task():
#     s = Bluevine()
#     assert s.task([2, 7, 11, 15]) == [2, 7, 11, 15]


def test(data: list) -> list:
    store = {}
    for item in data:
        if item not in store:
            store[item] = 1
        else:
            store[item] += 1
