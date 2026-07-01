class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[len(nums)-2]==1:
            return True
        return False
