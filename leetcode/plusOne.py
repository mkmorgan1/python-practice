# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Example 3:

# Input: digits = [0]
# Output: [1]


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # START AT THE LAST INDEX OF THE LIST
        i = len(digits) - 1

        while i >= 0:
            # IN THE CASE THAT WE REACH A 9 AT THE BEGINNING OF THE LIST:
            # LIKE: [9]
            if i == 0 and digits[i] == 9:
                digits[i] = 0
                digits.insert(0, 1)
                break
            # IN THE CASE THAT WE HAVE MULTIPLE 9S AT THE END OF THE LIST:
            # LIKE: [1, 0, 9, 9]
            elif digits[i] == 9:
                digits[i] = 0
                i += -1
            # MOST CASES:
            else:
                digits[i] = digits[i] + 1
                break

        return digits
