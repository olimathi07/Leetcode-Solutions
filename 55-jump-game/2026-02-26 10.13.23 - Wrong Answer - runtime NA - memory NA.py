class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[len(nums)-2]==1:
            return True
        if len(nums)==0:
            return True
        return False
