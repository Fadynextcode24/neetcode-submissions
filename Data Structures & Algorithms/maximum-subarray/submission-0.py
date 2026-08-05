class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        nums = [2,-3,4,-2,2,1,-1,4]
        Output: 8
        '''
        sumy=0
        maxy=float('-inf')
        for i in range(len(nums)):
            sumy=max(sumy+nums[i],nums[i])
            if (maxy<sumy):
                maxy=sumy
        return maxy