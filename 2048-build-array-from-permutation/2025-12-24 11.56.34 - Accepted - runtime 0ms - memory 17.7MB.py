class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(0,len(nums)):
            a.append(nums[nums[i]])
        return a