class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0 , len(prices) - 1
        max_profit = 0
        while l < r:
            profit = prices[r] - prices[l]
            if  profit < 0:
                l+=1
            else:
                r-=1
            max_profit = max(max_profit, profit)
        return max_profit