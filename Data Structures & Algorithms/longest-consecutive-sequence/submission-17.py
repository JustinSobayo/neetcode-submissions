class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_seen = set(nums)
        seq = 0
        for num in nums:
            #if we are at the beginning of the sequence, i am going to try to check if num+1 in nums_seen
            if (num - 1) not in nums_seen:
                curr_seq = 0
                while(num + curr_seq) in nums_seen:
                    curr_seq += 1
                seq = max(curr_seq, seq)
        return seq

        