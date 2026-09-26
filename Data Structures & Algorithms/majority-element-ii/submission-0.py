class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        bound = len(nums)/3
        nums_freq = {}
        answer = []
        for num in nums:
            nums_freq[num] = nums_freq.get(num, 0) + 1
        for num, freq in nums_freq.items():
            if nums_freq[num] > bound:
                answer.append(num)
        return answer


        