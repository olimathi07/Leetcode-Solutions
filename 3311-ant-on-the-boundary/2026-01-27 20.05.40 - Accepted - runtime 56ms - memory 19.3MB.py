class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        c=0
        t=0
        for i in nums:
            c+=i
            if c==0:
                t+=1
        
        return t