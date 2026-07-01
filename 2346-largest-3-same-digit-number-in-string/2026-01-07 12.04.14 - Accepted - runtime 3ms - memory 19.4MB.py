class Solution:
    def largestGoodInteger(self, num: str) -> str:
        r=""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                r=max(r,num[i:i+3])
        return r