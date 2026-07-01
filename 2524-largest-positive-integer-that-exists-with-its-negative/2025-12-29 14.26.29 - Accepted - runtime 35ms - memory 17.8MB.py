class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        p=[]
        n=[]
        for i in nums:
            if i>0:
                p.append(i)
            elif i<0:
                n.append(i)
        r=-1
        for i in p:
            if -i in n:
                r=max(r,i)
        return r