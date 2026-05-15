class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        hashmap = {}

        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = i
            else:
                hashmap[s[i]] = i

        print(hashmap)

        size = 0
        res = []
        last_index = hashmap[s[0]]

        for i in range(len(s)):
            size+=1
            last_index = max(last_index, hashmap[s[i]])
            if i == last_index:
                res.append(size)
                size = 0
        return res
            

        