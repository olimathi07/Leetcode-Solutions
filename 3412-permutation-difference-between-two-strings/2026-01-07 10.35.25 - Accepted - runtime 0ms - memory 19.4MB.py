class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        r=0
        for i in range(len(s)):
            d=s[i]
            r+=abs(i-t.index(d))
        return r