class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        c=Counter(s)
        r=""
        d=Counter(c.values())
        m=max(d,key=d.get)
        for k,v in c.items():
            if m==v:
                r+=k
        return r