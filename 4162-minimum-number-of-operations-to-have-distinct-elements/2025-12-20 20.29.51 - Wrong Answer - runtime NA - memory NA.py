from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=Counter(nums)
        if(i for i,c in c.items() if c<0):
            return 0