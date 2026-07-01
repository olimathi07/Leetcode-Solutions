class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while prod(map(int,str(n)))%t:
            n+=1
        return n
