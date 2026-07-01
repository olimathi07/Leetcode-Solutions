class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        k=set(nums1)&set(nums2)
        if not k:
            return -1
        return min(k)
        