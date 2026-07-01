class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l=[]
        c=Counter(nums)
        for k,v in c.items():
            if v==1:
                l.append(k)
        return l