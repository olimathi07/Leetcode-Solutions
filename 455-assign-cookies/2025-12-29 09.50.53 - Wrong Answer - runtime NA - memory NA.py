class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gs=sum(g)
        ss=sum(s)
        i,j=0,0
        c=0
        if ss>=gs:
            return len(g)
        else:
            while(len(g)>i and len(s)>j):
                if g[i]==s[j]:
                    c+=1
                    i+=1
                    j+=1
                elif g[i]>s[j]:
                    j+=1
                else:
                    i+=1
        return c
                




    