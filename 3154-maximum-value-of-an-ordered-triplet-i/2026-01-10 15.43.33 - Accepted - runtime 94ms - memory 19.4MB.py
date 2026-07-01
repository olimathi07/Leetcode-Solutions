class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        m=float('-inf')
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    m=max(m,(nums[i]-nums[j])*nums[k])
        if m<0:
            return 0
        return m