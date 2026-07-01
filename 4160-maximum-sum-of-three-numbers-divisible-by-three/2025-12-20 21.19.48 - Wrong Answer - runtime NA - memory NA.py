import array
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        n=len(nums)
        m=0
        for i in range(0,n):
            for j in range(i,n):
                s=0
                for k in range(i,j+1):
                    s+=nums[k]
                    if(s%3==0):
                        m=max(m,s)
        return m