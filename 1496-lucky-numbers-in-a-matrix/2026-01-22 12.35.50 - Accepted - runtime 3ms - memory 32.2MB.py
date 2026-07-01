import numpy as np
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        arr=np.array(matrix)
        m=np.min(arr,axis=1)
        n=np.max(arr,axis=0)
        r=[]
        for i in m:
            if i in n:
                r.append(int(i))
        return r