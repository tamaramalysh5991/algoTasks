# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = dict()
        result = []
        for i in range(len(nums)):
            differences[target - nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in differences and differences[complement] != i:
                return [i, differences[complement]]

        return result


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d:
                return [d[r], i]
            d[j] = i


print(Solution().twoSum([2,7,11,15], 9))
# print(Solution().twoSum([3, 2, 4], 6))
# print(Solution().twoSum([3,3], 6))
