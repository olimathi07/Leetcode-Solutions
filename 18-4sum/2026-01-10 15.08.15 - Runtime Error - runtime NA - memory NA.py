class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s=0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    for d in range(k,len(nums)):
                        if nums[i]+nums[j]+nums[k]+nums[d]==target:
                            s.append(nums[i])
                            s.append(nums[i])
                            s.append(nums[i])