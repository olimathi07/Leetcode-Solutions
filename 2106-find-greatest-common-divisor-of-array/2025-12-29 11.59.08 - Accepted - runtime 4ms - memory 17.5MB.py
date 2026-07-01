class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        s=nums[0]
        l=nums[len(nums)-1]
        return math.gcd(s,l)
       