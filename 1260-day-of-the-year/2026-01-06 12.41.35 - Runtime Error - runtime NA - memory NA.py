class Solution:
    def dayOfYear(self, date: str) -> int:
        l=[0,31,59,90,120,151,181,212,243,273,304,334]
        d=date[:-2]
        m=date[5:7]
        y=date[4:]
        if y%4!=0 and y!=1900 and m>3:
            d+=1
        return l[m-1]+d