
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)-1):
            string = s[i]
            if string not in s[i+1:-1]:
                return i




if __name__ == "__main__":
    # print(Solution().firstUniqChar("leetcode"))
    # print(Solution().firstUniqChar("loveleetcode"))
    print(Solution().firstUniqChar("aabb"))