class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0
        for i in range(1,len(prices)):
            sell = prices[i]
            diff = sell-buy
            profit=max(diff,profit)
            if sell<buy:
                buy=sell
        return profit


        