# Given an integer x, return true if x is a palindrome , and false otherwise.
# -231 <= x <= 231 - 1
# Could you solve it without converting the integer to a string?
class Solution:
    def isPalindrome(self, x: int) -> bool:
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

    def isPalindrome(self, n: int) -> bool:
        if n < 0:
            return False
        if n < 10:
            return True

        num_digits = 0
        divisor = 1
        while n // divisor >= 10:
            divisor *= 10
            num_digits += 1

        while n > 0:
            left_digit = n // divisor
            right_digit = n % 10
            if left_digit != right_digit:
                return False
            n = (n % divisor) // 10
            divisor //= 100
            num_digits -= 2
        return True


# if n < 0:
#         return False
#     if n < 10:
#         return True
#
#     rev = 0
#     x = n
#     while x > rev:
#         rev = rev * 10 + x % 10
#         x //= 10
#     return x == rev or x == rev // 10
def test_palindrome_number():
    s = Solution()
    assert s.isPalindrome(121) == True
    assert s.isPalindrome(-121) == False
    assert s.isPalindrome(10) == False
