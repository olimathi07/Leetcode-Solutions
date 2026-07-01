class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s=Counter(nums)
        l=[]
        for i,c in s.items():
            if c>=2:
                l.append(i)
        return l

