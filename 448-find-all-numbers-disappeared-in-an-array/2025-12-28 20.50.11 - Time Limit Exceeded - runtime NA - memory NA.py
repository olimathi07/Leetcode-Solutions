class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        l=[]
        n=len(nums)
        for i in range(len(nums)):
            if  i+1 not in nums:
                l.append(i+1)
        

        return l
        
