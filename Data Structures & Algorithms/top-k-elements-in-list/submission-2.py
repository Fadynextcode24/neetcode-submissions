class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq ={}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i]+=1
        s=[]
        for _ in range(k):
            max_num = None
            max_count = -1
            for i in freq:
                if freq[i] > max_count:
                    max_count = freq[i]
                    max_num = i
            s.append(max_num)
            del freq[max_num]
        return s