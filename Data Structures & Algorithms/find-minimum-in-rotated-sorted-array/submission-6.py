class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1 
        
        
        while l <= r:
            a = (l+r)//2

            if nums[l] < nums[r] or l==r:
                return nums[l]

            # if nums[a] < nums[a-1]:
            #     return nums[a]
            
            if nums[a] < nums[l]:
                r = a
            else:
                l = a + 1


        