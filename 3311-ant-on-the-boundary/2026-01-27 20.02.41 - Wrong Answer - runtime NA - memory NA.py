class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            c+=i
        return 0 if abs(c)>0 else 1