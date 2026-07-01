class Solution:
    def removeDuplicates(self, s: str) -> str:
        r=[]
        for i in s:
            if r and i==r[-1]:
                r.pop()
            else:
                r.append(i)
        return "".join(r)