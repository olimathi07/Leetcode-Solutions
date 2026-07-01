class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        p=[0]
        for i in range(n):
            p.append(p[i]+nums[i])
            m=max(0,i-nums[i])
            
            c+=(p[i+1]-p[m])
        return c