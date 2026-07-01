class Solution:
    def maxFreqSum(self, s: str) -> int:
        v=0
        c=0
        vi="aeiou"
        d=set(s)
        for i in d:
            if i in vi:
                v=max(v,s.count(i))
            else:
                c=max(c,s.count(i))
        return v+c
        