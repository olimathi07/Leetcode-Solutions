class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        r=0
        for i in range(len(s)):
            r+=abs(ord(s[i])-ord(t[i]))
        return r