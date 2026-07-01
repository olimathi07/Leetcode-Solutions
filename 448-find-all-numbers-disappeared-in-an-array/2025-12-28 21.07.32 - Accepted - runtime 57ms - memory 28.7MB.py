class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=[]
        n=len(nums)
        for i in range(len(nums)):
           id=abs(nums[i])-1
           nums[id]=-abs(nums[id])
        for i in range(n):
            if nums[i]>0:
                l.append(i+1)
        return l
        
