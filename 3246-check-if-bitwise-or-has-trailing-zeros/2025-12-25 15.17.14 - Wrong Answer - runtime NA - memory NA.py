class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
       
       for i in nums:
         if i%2==0:
           return True
       return False
    