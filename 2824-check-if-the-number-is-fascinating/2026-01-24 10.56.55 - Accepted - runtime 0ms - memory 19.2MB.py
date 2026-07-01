class Solution:
    def isFascinating(self, n: int) -> bool:
        t=0
        v="123456789"
        t=str(n)+str(2*n)+str(3*n)
        t=''.join(sorted(t))
        return v==t
    