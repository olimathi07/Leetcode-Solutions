class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n%2==1:
            return n
        else:
            return int(n/2)
