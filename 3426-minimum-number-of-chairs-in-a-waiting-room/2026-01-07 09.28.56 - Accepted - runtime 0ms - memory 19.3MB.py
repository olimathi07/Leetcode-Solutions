class Solution:
    def minimumChairs(self, s: str) -> int:
        c=0
        m=0
        for i in s:
            if i=='E':
                c+=1
            else:
                c-=1
            if c>m:
                m=c
               
        return m