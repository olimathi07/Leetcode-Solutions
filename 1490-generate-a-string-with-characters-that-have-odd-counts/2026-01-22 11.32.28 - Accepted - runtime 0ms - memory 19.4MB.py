class Solution:
    def generateTheString(self, n: int) -> str:
        s=""
        if n%2==0:
            s='o'*(n-1)
            s+='l'
        else:
            s='o'*n
        return s