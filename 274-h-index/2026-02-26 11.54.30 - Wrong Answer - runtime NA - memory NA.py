class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return citations[0]
        if len(citations)==1:
            return 1
