class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i,n in enumerate(nums):
            if n==target:
                l.append(i)
        if len(l)==1:
            return l*2
        if not l:
            return [-1,-1]
        return l