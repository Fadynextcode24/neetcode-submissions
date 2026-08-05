class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''Input: prices = [10,1,5,6,7,1]

        Output: 6'''
        l=0
        profit=0
        for i in range(len(prices)):
            l=i
            for j in range(l,len(prices)):
                diff = prices[j] - prices[l]
                if diff>profit:
                    profit=diff
        return profit




        