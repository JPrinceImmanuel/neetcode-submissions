class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:


        def bs(nums, l, r, target):
            if l > r and nums[l] > target:
                return l
            if l == r and nums[l] < target:
                return l + 1

            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return bs(nums, l, mid-1, target) 
            else:
                return bs(nums, mid+1, r, target)

        return bs(nums, 0, len(nums)-1, target)
        