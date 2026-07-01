class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        r=[]
    
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                r.append(nums[i:j])
        return len(r)