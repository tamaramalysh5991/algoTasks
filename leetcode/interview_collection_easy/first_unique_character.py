from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for key, value in c.items():
            if value == 1:
                return s.find(key)

        return -1


print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar("aabb"))

# ^ ?
# custom counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1