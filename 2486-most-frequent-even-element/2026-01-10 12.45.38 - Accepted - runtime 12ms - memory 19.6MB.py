class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c=Counter(i for i in nums if i%2==0)
        if not c:
            return -1
        d=max(c.values())
        return min(k for k,v in c.items() if v==d)
        

