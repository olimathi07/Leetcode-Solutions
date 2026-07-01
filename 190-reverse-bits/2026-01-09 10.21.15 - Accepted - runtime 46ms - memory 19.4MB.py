class Solution:
    def reverseBits(self, n: int) -> int:
        t=0
        for i in range(32):
            t=(t<<1)+(n&1)
            n>>=1
        return t
        