
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        offset = 0
        n = len(nums)
        for i in range(n):
            i = i - offset
            if i < (n-offset-1) and nums[i] == 0:
                nums.append(nums.pop(i))
                offset +=1
        return nums


nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
nums = [0]
Solution().moveZeroes(nums)
print(nums)
