class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmaps = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmaps:
                return [hashmaps[diff], i]
            hashmaps[n] = i
           

          