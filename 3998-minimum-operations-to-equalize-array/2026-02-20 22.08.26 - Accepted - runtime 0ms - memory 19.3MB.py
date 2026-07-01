class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s=set(nums)
        if len(s)==1:
            return 0
        return 1