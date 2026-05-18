class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hashmap = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in hashmap:
                hashmap[s[r]] +=1
            else:
                hashmap[s[r]] = 1

            frequency = (r-l+1) - max(hashmap.values())

            print(frequency)

            if frequency <= k:
                res = max(res, r-l+1)
            else:
                hashmap[s[l]] -=1
                l +=1
                    

        return res
            
            

            