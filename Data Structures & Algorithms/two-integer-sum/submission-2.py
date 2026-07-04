class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_seen = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in nums_seen:
                return [nums_seen[difference], i]
            nums_seen[num] = i
        return

        