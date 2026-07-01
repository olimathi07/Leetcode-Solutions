class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j=0,0
        c=0
        while(len(g)>i and len(s)>j):
            if g[i]<=s[j]:
                c+=1
                i+=1
            else:
                j+=1
        return c
                




    