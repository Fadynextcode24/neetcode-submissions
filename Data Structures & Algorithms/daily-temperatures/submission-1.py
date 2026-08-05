class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        n = len(temperatures)
        for i in range(n):
            count=1
            j=i+1
            while n > j:
                if temperatures[j]>temperatures[i]:
                    break
                j+=1
                count+=1
            if j == n:
                count =0
            s.append(count)
        return s
