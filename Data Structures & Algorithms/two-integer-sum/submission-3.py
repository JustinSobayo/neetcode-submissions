class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_seen = {}
        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in nums_seen:
                return [nums_seen[compliment], i]
            nums_seen[num] = i
            

