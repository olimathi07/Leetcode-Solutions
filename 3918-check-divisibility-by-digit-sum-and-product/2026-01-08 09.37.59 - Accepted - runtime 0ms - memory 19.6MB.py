class Solution:
    def checkDivisibility(self, n: int) -> bool:
        l=list(map(int,str(n)))
        s=int(sum(l))
        p=math.prod(l)
        return n%(s+p)==0
    