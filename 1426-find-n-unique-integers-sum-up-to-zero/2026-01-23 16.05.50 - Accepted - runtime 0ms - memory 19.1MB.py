class Solution:
    def sumZero(self, n: int) -> List[int]:
        l=[]
        i=0
        for j in range(1,n//2+1):
            l.append(j)
            l.append(-j)
        if n%2!=0:
            l.append(0)
        return l
        