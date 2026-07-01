class Solution:
    def countElements(self, nums: List[int]) -> int:
        m=min(nums)
        n=max(nums)
        c=0
        for i in nums:
            if i<n and i>m:
                c+=1
        return c
        
        