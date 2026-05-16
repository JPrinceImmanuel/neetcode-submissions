class Solution:
    def maxArea(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        max_res = 0

        while l <= r:
            length = min(nums[l], nums[r])
            breadth = r-l
            area = length * breadth

            max_res = max(max_res, area)
            if nums[l] < nums[r]:
                l+=1
            else:
                r-=1

        return max_res


        