class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        l1=[False]*n
        l2=[False]*m
        for i in range(0,n):
            for j in range(0,m):
                if matrix[i][j]==0:
                    l1[i]=True
                    l2[j]=True
        for i in range(0,n):
            for j in range(0,m):
                if l1[i] or l2[j]:
                    matrix[i][j]=0
        
        