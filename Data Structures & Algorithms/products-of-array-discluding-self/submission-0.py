class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        for i in range(n):
            proud=1
            for j in range(n):
                if i==j:
                    continue
                proud *= nums[j]
            ans.append(proud)
        return ans
        