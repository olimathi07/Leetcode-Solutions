class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        l=str(n)
        c=Counter(l)
        r=[]
        for k,v in c.items():
            if v==1:
                r.append(k)
        m=min(r)
        return int(m)
            