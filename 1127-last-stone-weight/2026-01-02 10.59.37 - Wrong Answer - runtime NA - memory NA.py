class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return len(stones)