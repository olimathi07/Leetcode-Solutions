class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if i%2!=0 and nums[i]%2==0:
                nums[i],nums[i+1]=nums[i+1],nums[i]
        return nums













            