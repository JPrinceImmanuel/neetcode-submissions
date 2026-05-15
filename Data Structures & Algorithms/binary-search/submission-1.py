class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bs(nums, l , r, target):
            if l > r:
                return -1

            mid = (l+r)//2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return bs(nums, mid+1, r, target)
            else:
                return bs(nums, l, mid-1, target)

        return bs(nums, 0, len(nums)-1, target)        