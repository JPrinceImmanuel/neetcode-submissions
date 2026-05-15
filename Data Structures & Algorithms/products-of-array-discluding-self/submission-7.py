class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         
         res = [0] * len(nums)

         for i , val_i in enumerate(nums):
            prod = 1
            for j, val_j in enumerate(nums):
                if i == j:
                    continue
                prod = prod * val_j
            res[i] = prod
         return res
        
                

        