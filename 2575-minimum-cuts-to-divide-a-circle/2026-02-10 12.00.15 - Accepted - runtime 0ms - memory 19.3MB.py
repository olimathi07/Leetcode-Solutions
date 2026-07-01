class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n==1:
            return 0
        elif n%2==1:
            return n
        
        return int(n/2)
