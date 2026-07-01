from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # l=permutations(nums)
        # r=[]
        # for i in l:
        #     r.append(i)
        return list(permutations(nums))