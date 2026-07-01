class Solution:
    def sortString(self, s: str) -> str:
        r=''
        s=list(s)
        while s:
            for i in sorted(set(s)):
                s.remove(i)
                r+=i
            for i in sorted(set(s),reverse=True):
                s.remove(i)
                r+=i
        return r
