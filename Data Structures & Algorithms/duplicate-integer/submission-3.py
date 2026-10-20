class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dupes = {}
        for num in nums:
            no_dupes[num] = no_dupes.get(num, 0)
        if len(no_dupes) == len(nums):
            return False
        else:
            return True        
        