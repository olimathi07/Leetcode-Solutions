class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        return sorted(nums,key=lambda i:(c[i],-i))