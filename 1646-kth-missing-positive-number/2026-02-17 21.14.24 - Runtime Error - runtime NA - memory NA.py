class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l=[i for i in range(1,1001) if i not in arr]
        return l[k-1]