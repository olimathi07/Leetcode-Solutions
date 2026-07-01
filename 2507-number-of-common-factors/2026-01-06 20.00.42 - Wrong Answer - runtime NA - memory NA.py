class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        r=[]
        l=[a,b]
        m=max(l)
        for i in range(1,m):
            if a%i==0 and b%i==0:
                r.append(i)
        return len(r)