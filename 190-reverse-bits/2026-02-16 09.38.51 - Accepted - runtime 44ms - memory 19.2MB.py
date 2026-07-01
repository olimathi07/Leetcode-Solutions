class Solution:
    def reverseBits(self, n: int) -> int:
        b = format(n, '032b')
        b=b[::-1]
        s=int(b,2)
        return s
        
        