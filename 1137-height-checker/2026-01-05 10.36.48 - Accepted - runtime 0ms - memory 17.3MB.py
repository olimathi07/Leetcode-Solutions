class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h=sorted(heights)
        c=0
        i=j=0
        while(i<len(h) and j<len(heights)):
                if heights[i]==h[j]:
                    i+=1
                    j+=1
                else:
                    c+=1
                    i+=1
                    j+=1
        return c