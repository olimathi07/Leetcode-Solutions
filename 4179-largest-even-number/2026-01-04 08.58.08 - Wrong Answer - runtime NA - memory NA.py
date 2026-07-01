class Solution:
    def largestEven(self, s: str) -> str:
        l=list(s)
        r=[]
        if int(s)%2==0:
            return s
        else:
            for i in l:
                if int(i)%2==0:
                    r.append(i)
        return "".join(r)
            