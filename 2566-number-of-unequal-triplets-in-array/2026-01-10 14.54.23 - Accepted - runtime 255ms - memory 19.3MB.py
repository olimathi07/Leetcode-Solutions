class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        c=0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if nums[i]!=nums[j] and nums[j]!=nums[k] and nums[k]!=nums[i]:
                        c+=1
        return c
                