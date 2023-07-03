from typing import List


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Can you come up with an algorithm that is less than O(n2) time complexity?
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, v in enumerate(nums):
            cache[v] = i
        for i, e in enumerate(nums):
            num = target - e
            if num in cache and i != cache[num]:
                return [i, cache[num]]
        return []


def test_two_sum():
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) in ([0, 1], [1, 0])
    assert s.twoSum([3, 2, 4], 6) in ([1, 2], [2, 1])
    assert s.twoSum([3, 3], 6) in ([0, 1], [1, 0])
