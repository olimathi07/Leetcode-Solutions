class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            i+=nums[i]
