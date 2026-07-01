class Solution:
    def minPartitions(self, n: str) -> int:
        arr=[int(i) for i in n]
        return max(arr)