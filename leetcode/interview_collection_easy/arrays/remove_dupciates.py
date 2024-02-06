from typing import List

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
class Solution:
    # dump soltuion
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = float("inf")
        nums.sort()
        print(nums)
        try:
            return nums.index(float("inf"))
        except ValueError:
            return len(nums)