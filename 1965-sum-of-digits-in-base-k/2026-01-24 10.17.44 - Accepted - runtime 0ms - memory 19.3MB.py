class Solution:
    def sumBase(self, n: int, k: int) -> int:
        r=0
        while n>0:
            t=n%k
            r+=t
            n//=k
        return r