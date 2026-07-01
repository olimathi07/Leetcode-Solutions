class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l=0
        r=len(s)
        t=[]
        for i in s:
            if i=='I':
                t.append(l)
                l+=1
            else:
                t.append(r)
                r-=1
        t.append(l)
        return t