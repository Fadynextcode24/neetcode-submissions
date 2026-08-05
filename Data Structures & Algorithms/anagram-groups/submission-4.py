class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            sorted1= "".join(sorted(i))
            if sorted1 not in d:
                d[sorted1] = []
            d[sorted1].append(i)
        return list (d.values())