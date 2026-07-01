class Solution:
    def residuePrefixes(self, s: str) -> int:
        c=0
        l=set()
        for i,n in enumerate(s):
            l.add(n)
            p=i+1
            if len(l)==p%3:
                c+=1
        return c