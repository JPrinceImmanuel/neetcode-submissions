class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        duplicates = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in duplicates:
                duplicates.remove(s[l])
                l +=1
                

            duplicates.add(s[r])
            max_len = max(max_len, (r-l)+1)

        return max_len



        