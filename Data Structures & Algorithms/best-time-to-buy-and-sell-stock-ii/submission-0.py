class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = float('inf')
        profit = 0
        #[7,1,5,3,6,4]
        for num in prices:
            if num < currMin:
                currMin = num
            else:
                profit += num - currMin
                currMin = num
        return profit

        
