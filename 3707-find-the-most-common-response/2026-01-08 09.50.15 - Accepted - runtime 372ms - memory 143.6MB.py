class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        c={}
        for i in responses:
            t=set(i)
            for j in t:
                if j in c:
                    c[j]+=1
                else:
                    c[j]=1
        m=max(c.values())
        r=sorted(i for i,v in c.items() if v==m)
        return r[0]