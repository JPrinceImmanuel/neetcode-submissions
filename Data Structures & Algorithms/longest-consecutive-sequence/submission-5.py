class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        if len(numset) != 0:
            max_count = 1
        else:
            max_count = 0

     
        for i in nums:
            count = 0
            if (i - 1) not in numset:
                count += 1
                for j in range(i+1, i+len(numset)+1):
                    if j in numset:
                        count+=1
                    else:
                        break
                    
                if count > max_count:
                    max_count = count

        return max_count
            
        