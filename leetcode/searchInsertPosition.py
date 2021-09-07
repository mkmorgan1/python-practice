# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        i = 0
        while i <= len(nums):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
            i += 1
