class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        no_dupes = set(nums)
        # [2,20,4,10,3,4,5]
        longest = 0
        for num in nums:
            current = 1
            while True:
                if num - 1 in no_dupes:
                    current += 1
                    num -= 1 
                else:
                    break
            longest = max(current, longest)
        return longest

