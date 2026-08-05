class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
        s=[]
        for _ in range(k):
            max_num = 0
            max_count = -1
            for i in d:
                if d[i] > max_count:
                    max_num = i
                    max_count = d[i]
            s.append(max_num)
            del d[max_num]
        return s



