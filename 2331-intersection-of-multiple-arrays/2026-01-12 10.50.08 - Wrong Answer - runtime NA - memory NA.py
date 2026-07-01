class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        c=Counter(nums[0])
        for i in nums[1:]:
            c&=Counter(i)
        return list(c.elements())
            