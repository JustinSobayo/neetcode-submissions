class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        nums_seen = {}
        #key: num, value:freq
        #at every index of freq represents the # of the numbers at the index
        #[0, [1,2], 0]
        #at index 1, 1 and 2 are in the nested array
        #this means that there is one 1 and one 2
        #now i have to go through the list and count the number of each number and assign each number to their spot
        for num in nums:
            nums_seen[num] = nums_seen.get(num, 0) + 1
        for key, value in nums_seen.items():
            freq[value].append(key)
        output = []
        for i in range(len(nums), -1, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) ==k:
                    return output
        return output


            