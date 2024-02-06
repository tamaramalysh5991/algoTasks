nums1 = [1,2,2,1]
nums2 = [2,2]

# [2,2]


# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # less_nums = nums1 if len(nums2) > len(nums1) else nums2
        less_nums = nums1
        bigger_nums = nums2
        if len(less_nums) > len(bigger_nums):
            less_nums, bigger_nums = less_nums, bigger_nums
        intersection = []
        for i in less_nums:
            if i in bigger_nums:
                intersection.append(i)
        return intersection



class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        i = j = 0
        k = []
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] == nums2[j]:
                k.append(nums1[i])
                j += 1
                i += 1
        return k


s = Solution()
# # n = [1,1,2]
# n = [0,0,1,1,1,2,2,3,3,4]
# print(s.intersect(nums1, nums2))
print(s.intersect([4,9,5], [9,4,9,8,4]))

