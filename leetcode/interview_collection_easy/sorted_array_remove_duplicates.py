from typing import List


# class Solution:
#     def removeDuplicates(self, nums):
#         # [1,1,2]
#         offset = 0
#         l = len(nums)
#         pred = nums[0]
#         for i in range(l):
#             i = i - offset
#             if i < (l-offset-1) and nums[i] == nums[i+1]:
#                 del nums[i+1]
#                 offset+=1
#         return len(nums)







# Миша, [30.05.21 17:06]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        offset = 0
        l = len(nums)
        for i in range(l):
            i = i - offset
            if i < (l-offset-1) and nums[i] == nums[i+1]:
                del nums[i+1]
                offset+=1
        return len(nums)


s = Solution()
# n = [1,1,2]
n = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(n))
print(n)

# def reverse(x: int) -> int:
#     res = [n for n in str(x)]
#     sym = ''
#     if not res[0].isdigit():
#         sym = res.pop(0)
#     res.reverse()
#     return int(f'{sym}{"".join(res)}')
#
#
# print(reverse(-123))