class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False

        hashmap = {}
        hand = sorted(hand)
        for i in hand:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i]+=1

        min_val = min(hashmap.keys())
        
        for i in range(1, len(hand)+1):
            if min_val in hashmap:
                hashmap[min_val] -=1
                if hashmap[min_val] == 0:
                    del hashmap[min_val]
                min_val += 1
            else:
                return False
                       
                
            if i % groupSize == 0 and len(hashmap.keys()) !=0 :
                min_val = min(hashmap.keys())

        return True


        

        