class Solution:
    def minWindow(self, s: str, t: str) -> str:

        res_len = float("inf")
        hash_t = {}
        have = 0
        hash_s = {}
        l = 0
        res = [-1, -1]

        for i in t:
            if i not in hash_t:
                hash_t[i] = 1
            else:
                hash_t[i]+=1

        for i in range(len(s)):
            if s[i] not in hash_s:
                hash_s[s[i]] = 1
            else:
                hash_s[s[i]] +=1

            if s[i] in hash_t and hash_s[s[i]] == hash_t[s[i]]:
                have+=1

            while have == len(hash_t):
                if i-l+1 < res_len:
                    res = [l, i]
                    res_len = i-l+1

                hash_s[s[l]] -=1
                if s[l] in hash_t and hash_s[s[l]] < hash_t[s[l]]:
                    have -=1

                l+=1

        l, i = res

        return s[l:i+1] 
        