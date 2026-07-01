class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        l=[]
        for i in edges:
            for j in i:
                
                l.append(j)
       
        c=Counter(l)
        return max(c,key=c.get)
            