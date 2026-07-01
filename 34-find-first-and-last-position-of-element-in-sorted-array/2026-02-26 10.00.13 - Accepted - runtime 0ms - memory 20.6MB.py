class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x=y=-1
        i=0
        for i,n in enumerate(nums):
            if n==target:
                if x==-1:
                    x=i
                y=i
        return [x,y]

