class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #[0, 2, 1, 2, 4]
        #compute prefix sum
        prefix = []
        prev = 0
        for num in nums:
            prefix.append(prev)
            prev += num
        prefix.append(prev)
        print(prefix)
        earlier_sum = {}
        count = 0
        for num in prefix:
            if num - k in earlier_sum:
                count += earlier_sum[num-k]
            print(count)
            earlier_sum[num] = earlier_sum.get(num, 0) + 1
        return count
        