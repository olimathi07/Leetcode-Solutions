class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        s=nums[0]
        l=nums[len(nums)-1]
        while(l!=0):
            c=l
            l=s%l
            s=c
        return c
       