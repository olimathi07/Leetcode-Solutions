class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s)
        o,e=0,len(s)
        m=0
        for k,v in c.items():
            if v%2==0:
                e=max(v,e)
            else:
                o=max(o,v)
        return o-e
        