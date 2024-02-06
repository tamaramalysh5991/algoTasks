from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n:
            if m and nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

num1 = [1,2,3,0,0,0]
Solution().merge(num1, 3, [2,5,6], 3)

print(num1)



def merge_sorted_lists(listA, listB):
    merged = []
    i = 0
    j = 0

    while i < len(listA) and j < len(listB):
        if listA[i] <= listB[j]:
            merged.append(listA[i])
            i += 1
        else:
            merged.append(listB[j])
            j += 1


    while i < len(listA):
        merged.append(listA[i])
        i += 1

    while j < len(listB):
        merged.append(listB[j])
        j += 1

    return merged


# print(merge_sorted_lists([1,2,3], [2,5,6]))