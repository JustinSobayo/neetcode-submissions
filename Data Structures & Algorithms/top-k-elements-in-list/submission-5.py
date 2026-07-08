class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums)+1)]
        answer = []
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for key, value in count.items():
            frequency[value].append(key)
        for i in range(len(frequency) - 1, -1, -1):
            for num in frequency[i]:
                answer.append(num)
            if len(answer) == k:
                return answer
        
        
