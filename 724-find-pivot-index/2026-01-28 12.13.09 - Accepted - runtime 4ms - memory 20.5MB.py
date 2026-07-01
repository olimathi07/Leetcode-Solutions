class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        l=0
        for i in range(len(nums)):
            if l==s-l-nums[i]:
                return i
            else:
                l+=nums[i]
        return -1
        