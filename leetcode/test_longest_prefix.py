# Write a function to find the longest common prefix string amongst an array of strings.
from itertools import zip_longest
from typing import List


# If there is no common prefix, return an empty string "".
# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# https://leetcode.com/problems/longest-common-prefix/
def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ""
    for data in zip_longest(*strs):
        if all(data) and len(set(data)) == 1:
            prefix += data[0]
        else:
            break
    return prefix


def test_longestCommonPrefix():
    assert longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert longestCommonPrefix(["dog", "racecar", "car"]) == ""
