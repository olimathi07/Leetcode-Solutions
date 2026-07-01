class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set(nums1)
        s2=set(nums2)
        l=sum(1 for i in nums1 if i in nums2)
        r=sum(1 for i in nums2 if i in nums1)
        return[l,r]