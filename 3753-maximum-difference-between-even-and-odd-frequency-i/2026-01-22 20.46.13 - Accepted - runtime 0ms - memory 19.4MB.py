class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s)
        o,e=0,len(s)
        m=0
        for v in c.values():
            if v%2==0:
                e=min(v,e)
            else:
                o=max(o,v)
        return o-e
        