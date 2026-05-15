class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        good = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            if t[0] == target[0]:
                good.add(t[0])

            if t[1] == target[1]:
                good.add(t[1])

            if t[2] == target[2]:
                good.add(t[2])
        print(good)
        return len(good) == len(set(target))
            
           

            
            
        