class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s)
        o,e=[],[]
        for k,v in c.items():
            if v%2==0:
                e.append(v)
            else:
                o.append(v)
        return max(o)-max(e)