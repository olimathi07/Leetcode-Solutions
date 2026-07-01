class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
       
       for i in range(len(nums)):
         for j in range (len(nums)):
            if i!=j and (nums[i]|nums[j])%2==0:
                return True
       return False
         
    