class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        t=Counter(nums)
        s=0
        for i in nums:
            if t[i]==1:
                s+=i
        return s   