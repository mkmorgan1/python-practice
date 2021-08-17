# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        t = ''
        x = str(x)

        i = len(x) - 1
        while i >= 0:
            t += x[i]
            i -= 1

        if t == x:
            return True
        else:
            return False
