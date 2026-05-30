class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j=[]
        for i in range(len(nums)):
            for j in range(1+i,len(nums)):
                difference = target - nums[i]
                if nums[j]==difference:
                    return[i,j]