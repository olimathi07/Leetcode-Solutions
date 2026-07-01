class Solution:
    def secondHighest(self, s: str) -> int:
        l=set()
        for i in s:
            if i.isdigit():
                l.add(int(i))
        r=list(l)
        r.sort()
        return r
        