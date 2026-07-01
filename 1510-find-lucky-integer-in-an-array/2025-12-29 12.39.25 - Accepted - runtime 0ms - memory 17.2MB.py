class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c=Counter(arr)
        l=[]
        for k,v in c.items():
            if k==v:
                l.append(k)
        if not l:
            return -1
        else:
            return max(l)
        