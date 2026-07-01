class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        r=set(nums[0])
        for i in range(1,len(nums)):
            r&=set(nums[i])
        r=list(r)
        r.sort()
        return r
            