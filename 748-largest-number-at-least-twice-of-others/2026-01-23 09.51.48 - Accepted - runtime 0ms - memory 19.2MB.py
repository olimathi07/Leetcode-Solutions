class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)
        i=nums.index(m)
        for k in nums:
            if k!=m and m<2*k:
                return -1
        return i