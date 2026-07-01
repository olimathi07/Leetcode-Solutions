class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        m=float('inf')
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]>=nums[j]:
                    continue
                for k in range(j+1,n):
                    if nums[k]>=nums[j]:
                        continue
                    m=min(m,nums[i]+nums[j]+nums[k])
        if m==float('inf'):
            return -1
        return m