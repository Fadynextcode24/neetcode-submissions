class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for i in strs:
            sorted1 = "".join(sorted(i))
            if sorted1 not in m:
                m[sorted1] = []

            m[sorted1].append(i)
        return list(m.values())



        