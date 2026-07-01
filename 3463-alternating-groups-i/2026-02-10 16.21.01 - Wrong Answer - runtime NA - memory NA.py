class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        c=0
        for i in range(len(colors)):
            if colors[i]!=colors[(i+1)%2]:
                c+=1
        return c