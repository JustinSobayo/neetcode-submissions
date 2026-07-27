class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices = [[5,1,5,6,7,1,10]
        #.            l r
        minPrice = float('inf')
        l = 0
        r = 1
        maxPrice = 0
        while r < len(prices):
            while prices[r] < prices[l] and r + 1 < len(prices):
                l = r
                r += 1
            maxPrice = max(maxPrice, prices[r] - prices[l])
            r += 1
        return maxPrice


        