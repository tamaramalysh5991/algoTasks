from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k % len(nums)):
            nums.insert(0, nums.pop())

nums = [1,2,3,4,5,6,7]
Solution().rotate(nums, 3)
print(nums)

def shift(lst, steps):
    steps = abs(steps)
    for i in range(steps):
        lst.append(lst.pop(0))