class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        arr=[]
        if m*n != r*c:
            return mat
    
        for i in mat:
            for j in i:
                arr.append(j)
        t=[]
        idx=0
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(arr[idx])
                idx+=1
            t.append(row)
        return t
                    
