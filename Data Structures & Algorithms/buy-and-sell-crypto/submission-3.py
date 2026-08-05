class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''Input: prices = [10,1,5,6,7,1]

        Output: 6'''
        l=0
        profit=0
        for i in range(1,len(prices)):
            if prices[i]<prices[l]:
                l=i
            diff = prices[i]-prices[l]
            if diff>profit:
                profit=diff
        return profit






        