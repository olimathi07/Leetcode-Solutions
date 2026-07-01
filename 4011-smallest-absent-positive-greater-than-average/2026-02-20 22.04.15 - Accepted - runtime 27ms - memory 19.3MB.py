class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        a=sum(nums)/len(nums)
        nums.append(a)
        for i in range(1,202):
            if i not in nums and i>a:
                return i
        