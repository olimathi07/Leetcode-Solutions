class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l=[]
        for i,n in enumerate(nums):
            if n==target:
                l.append(i)
        return l