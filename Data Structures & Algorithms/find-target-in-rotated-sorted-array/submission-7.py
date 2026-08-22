class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        res = -1
        #[3,4,5,6,1,2], target = 6
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if target > nums[m]:
                    l = m + 1
                elif target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            #right portion of the rotation
            else:
                if target < nums[m]:
                    r = m - 1
                elif target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return res