class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         
         res = [0] * len(nums)

         for i , val_i in enumerate(nums):
            product = 1
            for j, val_j in enumerate(nums):
                if i == j:
                    continue
                product = product * val_j
            res[i] = product
         return res
        
                

        