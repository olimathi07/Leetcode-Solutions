from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        while len(nums)!=len(set(nums)):
            c+=1
            nums=nums[3:]
        return c
            