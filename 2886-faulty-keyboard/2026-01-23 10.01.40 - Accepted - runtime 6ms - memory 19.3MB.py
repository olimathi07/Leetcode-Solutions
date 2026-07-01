class Solution:
    def finalString(self, s: str) -> str:
        r=""
        for i in s:
            if i!='i':
                r+=i
            else:
                r=r[::-1]
        return r
