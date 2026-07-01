class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        c=0
        for i in colors:
            if i==0 and i+1==1:
                c+=1
            elif i==1 and i+1==0:
                c+=1
        return c