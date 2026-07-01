class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=Counter(nums)
        m=max(c.values())
        s=0
        for k,v in c.items():
            if v==m:
                s+=v
        return s