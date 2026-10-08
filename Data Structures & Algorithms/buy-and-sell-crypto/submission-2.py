class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minVal = prices[0]
        for i in range(len(prices)):
            profit = prices[i] - minVal
            maxProfit = max(maxProfit, profit)
            minVal = min(minVal, prices[i])
        return maxProfit