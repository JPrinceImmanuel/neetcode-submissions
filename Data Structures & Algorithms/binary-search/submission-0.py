class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left_pointer = 0
        right_pointer = len(nums) -1 
        
        while left_pointer <= right_pointer:
            a = (left_pointer + right_pointer)//2
            
            if nums[a] < target:
                left_pointer = a + 1
            elif nums[a] > target:
                right_pointer = a -1
            else:
                return a
        return -1

        