class Solution:
    def modifyString(self, s: str) -> str:
        r=""
        for i in s:
            if i=='?':
                r+='a'
            else:
                r+=i
        return r