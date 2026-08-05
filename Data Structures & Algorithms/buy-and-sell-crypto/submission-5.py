class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max1=0
        for i in range(len(prices)):
            buy=prices[i]
            for j in range(i+1,len(prices)):
                sell = prices[j]
                max1= max(max1,prices[j]-prices[i])
        return max1



        