class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums.sort()
        t=1
        for i in nums:
            if i>0 and i==t:
                t+=1
            elif i>t:
                return t
            return t

               