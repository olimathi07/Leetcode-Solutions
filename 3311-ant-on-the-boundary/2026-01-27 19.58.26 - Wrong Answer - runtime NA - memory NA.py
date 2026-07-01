class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if i>0:
                c+=1
            else:
                c-=1
        return c