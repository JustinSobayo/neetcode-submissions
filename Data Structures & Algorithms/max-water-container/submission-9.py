class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights) - 1
        while l <r:
            length = r - l
            height = min(heights[l], heights[r])
            curr = length * height
            area = max(curr, area)
            if heights[l] <= heights[r]:
                l +=1
            else:
                r -= 1
        return area