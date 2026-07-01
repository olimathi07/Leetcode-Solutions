class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        c=Counter(nums)
        f=Counter(c.values())
        for n in nums:
            if f[c[n]]==1:
                return n
        return -1