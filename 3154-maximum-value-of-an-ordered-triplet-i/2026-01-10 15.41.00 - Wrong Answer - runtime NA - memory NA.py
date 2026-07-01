class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        m=float('-inf')
        n=len(nums)
        for i in range(0,n):
            for j in range(i,n):
                for k in range(j,n):
                    if nums[i]>0 and nums[j]>0 and nums[k]>0:
                        m=max(m,(nums[i]-nums[j])*nums[k])
                    else:
                        return 0
        return m