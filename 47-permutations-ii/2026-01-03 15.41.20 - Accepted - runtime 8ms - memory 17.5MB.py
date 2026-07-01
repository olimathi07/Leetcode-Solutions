from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # r=set()
        # p=permutations(nums)
        # for i in p:
        #     r.add(i)
        # s=list(r)
        return list(set(permutations(nums)))