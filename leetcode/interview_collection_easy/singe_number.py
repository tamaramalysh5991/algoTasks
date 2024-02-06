from typing import List

# nums = [2,2,1]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dupe = 0
        for i in nums:
            dupe = dupe ^ i

        return dupe