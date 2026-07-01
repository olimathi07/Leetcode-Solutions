class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1=set(nums1)
        s2=set(nums2)
        a=list(s1-s2)
        b=list(s2-s1)
        return [a,b]