class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        
        res = 0

        for i in range(len(s)):
            duplicates = set()
            for j in range(i , len(s)):
                if s[j] in duplicates:
                    break
                res = max(res, j-i+1)
                duplicates.add(s[j])

        return res



        