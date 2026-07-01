class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        nums.sort()
        for i,n in enumerate(nums):
            if n==target:
                l.append(i)
        if target not in nums:
            l.append(-1)
            l.append(-1)
        return l