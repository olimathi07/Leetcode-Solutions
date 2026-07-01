class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        return sum(set(arr))%k==0