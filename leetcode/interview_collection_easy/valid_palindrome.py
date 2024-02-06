from collections import Counter

class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = Counter(''.join(x for x in s.lower() if x.isalpha()))
        once_odd = 0
        for v in c.values():
            if v == 1 and not once_odd:
                once_odd += 0
                continue
            if v == 1 and once_odd:
                return False
            if v % 2 != 0:
                return False
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = [x for x in s.lower() if x.isalnum()]
        # return c == list(reversed(c))
        return c == c[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

print(Solution().isPalindrome('A man, a plan, a canal: Panama'))
print(Solution().isPalindrome('race a car'))
print(Solution().isPalindrome('ab'))