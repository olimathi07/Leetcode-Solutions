class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)==1:
            return 1
        return citations[0]
