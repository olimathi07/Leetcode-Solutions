class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        a=sum(nums)/len(nums)
        nums.append(a)
        nums.sort()
        return nums[len(nums)-1]+1