class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        s=list(set(nums))
        s.sort()
        l=[]
        if len(s)>2:
            l.append(s[len(s)-1])
            l.append(s[len(s)-2])
            l.append(s[len(s)-3])
            return l
        else:
            r=sorted(s,reverse=True)
            return r
        