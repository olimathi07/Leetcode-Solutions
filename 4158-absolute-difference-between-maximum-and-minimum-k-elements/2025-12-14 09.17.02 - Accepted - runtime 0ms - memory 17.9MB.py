class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
      nums.sort()
      m=sum(nums[:k])
      n=sum(nums[-k:])
      return abs(n-m)