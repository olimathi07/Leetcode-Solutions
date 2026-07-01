class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums)==3:
            return sum(nums)
        return 0