class Solution:
    def lengthOfLongestSubstring_(self, s: str) -> int:
        if not s:
            return 0
        i = j = 0
        res = set()
        max_len = 0
        while j < len(s):
            print(s[j])
            if s[j] not in res:
                res.add(s[j])
                j += 1
                continue
            max_len = max(max_len, len(list(res)))
            i = j
            res = set()

        max_len = max(max_len, len(list(res)))
        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = 0
        start = 0

        for i, el in enumerate(s):
            if el in seen:
                start = max(start, seen[el] + 1)
            seen[el] = i
            max_length = max(max_length, i - start + 1)

        return max_length


s = Solution()
# print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("abcabcbb"))
# print(s.lengthOfLongestSubstring("au"))
# print(s.lengthOfLongestSubstring("aab"))
print(s.lengthOfLongestSubstring("dvdf"))
