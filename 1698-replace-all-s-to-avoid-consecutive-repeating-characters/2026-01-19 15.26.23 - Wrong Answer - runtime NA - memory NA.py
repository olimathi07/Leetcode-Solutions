class Solution:
    def modifyString(self, s: str) -> str:
        arr=list(s)
        for i in range(len(arr)):
            if arr[i]=='?':
                arr[i]='a'
        return arr