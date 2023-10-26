# https://leetcode.com/problems/palindrome-number/
# Given an integer x, return true if x is a palindrome , and false otherwise.
# -231 <= x <= 231 - 1
# Could you solve it without converting the integer to a string?


def isPalindromeV1(x: int) -> bool:
    if x < 0:
        return False
    if x < 10:
        return True
    orig = x
    rev = 0
    while x:
        rev = rev * 10 + x % 10
        x //= 10
    return rev == orig


def isPalindromeV2(n: int) -> bool:
    reversed_num = 0
    temp = n
    while temp > 0:
        reversed_num = (reversed_num << 1) | (temp & 1)
        temp = temp >> 1

    return n == reversed_num


# def test_palindrome_numberV1(benchmark):
#     result = benchmark.pedantic(isPalindromeV1, args=(12345678987654321,), iterations=10000, rounds=100)
#
#     assert result is True


def test_palindrome_numberV1_palindromes():
    # numbers = [0, 121, 12321, 1234321]
    numbers = [121]
    results = []
    for number in numbers:
        result = isPalindromeV2(number)
        results.append(result)

    assert results == [True, True, True, True]


# def test_palindrome_numberV1_non_palindromes(benchmark):
#     numbers = [123, 12345, 1234567, -121, 5, 12345678987654321]
#     results = []
#     for number in numbers:
#         result = isPalindromeV1(number)
#         results.append(result)
#
#     assert results == [False, False, False, False, True, True]
