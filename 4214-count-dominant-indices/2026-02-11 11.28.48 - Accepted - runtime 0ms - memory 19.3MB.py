class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        t = sum(nums)
        count = 0
        n=len(nums)

        for num in nums:
            t-=num
            n-=1
            count+=(n*num)>t
            

        return count