class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dupe = set(nums)
        if len(no_dupe) != len(nums):
            return True
        else:
            return False
        