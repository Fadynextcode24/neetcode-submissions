class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        n=len(temperatures)
        for i in range(n):
            count=1
            j=i+1
            while j<n:
                if temperatures[j] > temperatures[i]:
                    break
                count+=1
                j+=1
            if j==n:
                count=0
            s.append(count)
        return s

