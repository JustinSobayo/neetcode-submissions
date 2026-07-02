class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashed = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_hashed:
                return [nums_hashed[diff], i]
            nums_hashed[n] = i
        return


