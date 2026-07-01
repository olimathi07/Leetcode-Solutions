class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        a=nums[0]
        for i,j in pairwise(nums):
            if j-i==1: a+=j
            else: break
        while a in nums: a+=1
        return a