class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        l=[]
        for i in range(len(height)-1):
            if height[i]>threshold:
                l.append(i+1)
        return l
        