class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        max1=0
        for i in range(1,len(prices)):
            sell=prices[i]
            profit= sell-buy
            max1 = max(max1,profit)
            if sell < buy:
                buy=sell
        return max1




        