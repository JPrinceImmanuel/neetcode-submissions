class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        l = 0
        s1_hashmap = {}
        s2_hashmap = {}
        
        for i in range(len(s1)):
            if s1[i] in s1_hashmap:
                s1_hashmap[s1[i]] +=1
            else:
                s1_hashmap[s1[i]] = 1

        for r in range(len(s2)):
            if s2[r] in s2_hashmap:
                s2_hashmap[s2[r]] +=1
            else:
                s2_hashmap[s2[r]] = 1
            
            if s1_hashmap == s2_hashmap:
                    return True

            while r-l+1 > len(s1):
                s2_hashmap[s2[l]] -=1
                if s2_hashmap[s2[l]] == 0:
                    del s2_hashmap[s2[l]]
                l+=1

            if s1_hashmap == s2_hashmap:
                return True
            
        return False

        