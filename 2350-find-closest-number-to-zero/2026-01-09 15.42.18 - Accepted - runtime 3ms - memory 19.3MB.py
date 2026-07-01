class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        r=float('inf')
        for i in nums:
            r=min(abs(i),r)
        return r if r in nums else -r
            