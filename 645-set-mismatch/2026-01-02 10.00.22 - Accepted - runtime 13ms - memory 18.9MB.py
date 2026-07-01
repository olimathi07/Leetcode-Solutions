class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        r=set()
        d=-1
        for i,n in enumerate(nums):
            if n in r:
                d=n
            else:
                r.add(n)
        for i in range(1,len(nums)+1):
            if i not in r:
                m=i
        return [d,m]


        return r