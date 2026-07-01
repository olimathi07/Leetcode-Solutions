class Solution:
    def averageValue(self, nums: List[int]) -> int:
        l=[]
        s=0
        for i in nums:
            if i%3==0 and i%2==0:
                l.append(i)
        if len(l)>0:
            return int(sum(l)/len(l))
        return 0

        
