class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        t=-1
        for l in range(len(s)):
            for r in range(l+1,len(s)):
                if s[l]==s[r]:
                    t=max(t,r-l-1)
        return t