class Solution:
    def trap(self, height: List[int]) -> int:
        #height = [0,2,0,3,1,0,1,3,2,1]
        #.           l               r
        r = len(height) - 1
        l = 0
        if not height: return 0
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l +=1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -=1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res


