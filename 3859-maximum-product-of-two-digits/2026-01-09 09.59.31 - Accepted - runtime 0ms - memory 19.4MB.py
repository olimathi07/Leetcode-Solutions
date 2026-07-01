class Solution:
    def maxProduct(self, n: int) -> int:
        m=0
        l=list(map(int,str(n)))
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                d=l[i]*l[j]
                m=max(d,m)
        return m
