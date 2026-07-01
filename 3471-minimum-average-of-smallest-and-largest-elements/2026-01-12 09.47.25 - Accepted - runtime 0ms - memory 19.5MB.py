class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        m=float('inf')
        for i in range(0,len(nums)//2):
            avg=(nums[i]+nums[len(nums)-i-1])/2
            m=min(avg,m)
        return m