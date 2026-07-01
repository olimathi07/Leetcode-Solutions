class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        r=[]
        for k,v in c.items():
            if v==2:
                r.append(k)
        return r