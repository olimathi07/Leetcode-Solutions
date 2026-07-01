class Solution:
    def countDigits(self, num: int) -> int:
        l=list(map(int,str(num)))
        c=0
        for i in l:
            if num%i==0:
                c+=1
        if c==0:
            return 1
        return c