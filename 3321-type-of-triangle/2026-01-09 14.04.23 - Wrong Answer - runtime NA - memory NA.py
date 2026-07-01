class Solution:
    def triangleType(self, nums: List[int]) -> str:
        s=set(nums)
        if len(s)==3:
            return "scalene"
        elif len(s)==2:
            return "isosceles"
        else:
            return "equilateral"