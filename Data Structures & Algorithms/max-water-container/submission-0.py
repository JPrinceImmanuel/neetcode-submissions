class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0

        right_pointer = len(heights) -1 
        left_pointer = 0

        while left_pointer < right_pointer:
            area = (right_pointer - left_pointer) * min(heights[left_pointer], heights[right_pointer]) 
            res = max(res, area)

            if heights[left_pointer] < heights[right_pointer]:
                left_pointer = left_pointer + 1
            elif heights[right_pointer] < heights[left_pointer]:
                right_pointer = right_pointer - 1
            else:
                right_pointer = right_pointer -1
        return res


        