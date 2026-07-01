class Solution:
    def residuePrefixes(self, s: str) -> int:
        c=0
        n=len(s)
        for i in s:
            if len(i)%3!=0:
                c+=1
        return c-1