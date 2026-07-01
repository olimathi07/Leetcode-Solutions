class Solution:
    def hammingWeight(self, n: int) -> int:
        k=bin(n)[2:]
        return k.count('1')