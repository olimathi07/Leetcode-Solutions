class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=l:
                l=i
        return True if l==0 else False
