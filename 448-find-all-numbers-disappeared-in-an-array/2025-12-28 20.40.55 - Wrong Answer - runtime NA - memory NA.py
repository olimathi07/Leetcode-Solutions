class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        l=[]
        for i in range(1,len(nums)):
            if  nums[i]!=i:
                l.append(i)
        if not l:
            l.append(len(nums))

        return l
        
