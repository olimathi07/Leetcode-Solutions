import array
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        n=len(nums)
        m=0
        for i in range(0,n):
            for j in range(i+1,n):
                s=0
                for k in range(j+1,n):
                    s=nums[i]+nums[j]+nums[k]
                    if(s%3==0):
                        m=max(m,s)
        return m