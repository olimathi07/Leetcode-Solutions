class Solution:
    def removeStars(self, s: str) -> str:
        a=list(s)
        r=[]
        for i in a:
            if i=='*':
                r.pop()
            else:
                r+=[i]
        return "".join(r)
                