class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        l=str(n)
        c=Counter(l)
        r=[]
        mi=min(c.values())
        for k,v in c.items():
            if v==mi:
                r.append(k)
        m=min(r)
        return int(m)
            