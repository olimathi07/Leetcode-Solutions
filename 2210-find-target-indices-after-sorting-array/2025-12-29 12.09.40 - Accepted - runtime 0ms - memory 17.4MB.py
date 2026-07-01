class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l=[]
        nums.sort()
        for i,n in enumerate(nums):
            if n==target:
                l.append(i)
        return l