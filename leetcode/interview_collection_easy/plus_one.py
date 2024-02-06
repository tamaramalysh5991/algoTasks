'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''

from typing import *

class Solution:
    # dump solution
    def plusOne(self, digits: List[int]) -> List[int]:
        res = int(''.join([str(x) for x in digits])) + 1
        return [int(x) for x in str(res)]


s = Solution()
print(s.plusOne([9]))
print(s.plusOne([4,3,2,1]))
print(s.plusOne([1,2,3]))
print(s.plusOne([9, 9]))

[9,9]

[1,0,0]

# better solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # move along the input array starting from the end
        for idx in reversed(range(n)):
            # reverse?
            # idx = n - 1 - i
            # set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1
                digits[idx] += 1
                # and the job is done
                return digits

        # we're here because all the digits are nines
        return [1] + digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            carry, digits[i] = divmod(digits[i] + carry, 10)

        return digits if not carry else [carry] + digits


s = Solution()
print(s.plusOne([9]))
print(s.plusOne([4,3,2,1]))
print(s.plusOne([1,2,3]))
print(s.plusOne([9, 9]))