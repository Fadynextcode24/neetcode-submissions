class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''Input: height = [1,7,2,5,4,7,3,6]

        Output: 36
        '''
        curr=0
        maxy=0
        l,r=0,len(heights)-1
        while l<r:
            if heights[l]< heights[r]:
                curr = heights[l] * (r-l)
                l=l+1
            else:
                curr = heights[r] * (r-l)
                r=r-1
            if curr>maxy:
                maxy=curr
            high = max(curr,maxy)
        return high
