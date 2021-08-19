# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.


class Solution:
    def removeElement(self, nums, val: int) -> int:
        if val in nums:
            nums.remove(val)
            self.removeElement(nums, val)
        else:
            print(nums)
            print(len(nums))


test = Solution()
test.removeElement([1, 2, 3, 4, 5, 5], 5)
