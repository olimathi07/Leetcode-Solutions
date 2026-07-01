class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        if len(nums)==2: return 1
        s=set()
        while nums:
            m=min(nums)
            n=max(nums)
            s.add((m+n)/2)
            nums.remove(n)
            nums.remove(m)
        return len(s)