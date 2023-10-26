# Given a list of words L, find all the anagrams in L in the order in which they appear in L.
# An anagram of a string is another string that contains same characters, only the order of characters can be different
# An Example
# Given the input
# ["pool", "loco", "cool", "stain", "satin", "pretty", "nice", "loop", "pool"]
# The desired output would be
# ["pool", "loco", "cool", "stain", "satin", "loop",  "pool"]
# in that order exactly.
from collections import Counter

def isAnagram(str1, str2):
    return sorted(list(str1)) == sorted(list(str2))

def main(data):
    ret = []
    for i in range(len(data)):
        for j in range(len(data)):
            if isAnagram(data[i], data[j]) and i != j:
                ret.append(data[i])
                break
    print(ret)
    return ret


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(["pool", "loco", "cool", "stain", "satin", "pretty", "nice", "loop", "pool"])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
