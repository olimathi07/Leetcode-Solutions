class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n%2==1:
            return n
        elif n==1:
            return 0
        
        return int(n/2)
