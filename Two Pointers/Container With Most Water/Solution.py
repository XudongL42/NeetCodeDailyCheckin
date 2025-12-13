class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = min(heights[0], heights[-1])*(len(heights)-1)
        left, right = 0, len(heights)-1
        while left < right:
            new_area = min(heights[left], heights[right])*(right-left)
            max_area = new_area if new_area > max_area else max_area
            if heights[left] < heights[right]:
                # pick the higher one
                left += 1
            else:
                right -= 1
        return max_area