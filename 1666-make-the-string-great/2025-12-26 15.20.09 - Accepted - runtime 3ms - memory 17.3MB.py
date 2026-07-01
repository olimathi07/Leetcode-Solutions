class Solution:
    def makeGood(self, s: str) -> str:
        if len(s)==1:
            return s
        r=[]
        for i in s:
            if r and abs(ord(i)-ord(r[-1]))==32:
                r.pop()
            else:
                r+=[i]
        return "".join(r)