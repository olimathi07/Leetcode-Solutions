class Solution:
    def specialArray(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if i!=0:
                c+=1
        if c==0:
            return -1
        return c