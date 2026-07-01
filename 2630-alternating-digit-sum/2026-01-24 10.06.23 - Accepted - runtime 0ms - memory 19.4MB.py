class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=str(n)
        r=0
        for i in range(0,len(s),2):
            r+=int(s[i])
        for i in range(1,len(s),2):
            r-=int(s[i])
        return r