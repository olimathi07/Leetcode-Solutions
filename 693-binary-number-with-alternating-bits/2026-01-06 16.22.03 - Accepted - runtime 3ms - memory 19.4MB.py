class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b=bin(n)[2:]
        return "00" not in b and "11" not in b