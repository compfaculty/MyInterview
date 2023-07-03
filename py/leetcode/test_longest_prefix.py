# Write a function to find the longest common prefix string amongst an array of strings.
from typing import List

# If there is no common prefix, return an empty string "".
# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


def longestCommonPrefix(strs: List[str]) -> str:
    return ""


def test_longestCommonPrefix():
    assert longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert longestCommonPrefix(["dog", "racecar", "car"]) == ""
