import numpy as np
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        m=0
        for i in range(0,len(points)):
            m=max(m,points[i][0]-points[i-1][0])
        return m