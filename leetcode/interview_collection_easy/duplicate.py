from collections import defaultdict
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = defaultdict(int)
        for i in nums:
            dups[i] += 1
            if dups[i] >= 2:
                return True