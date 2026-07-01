class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x=y=n
        s=0
        p=1
        while(x!=0):
            r=x%10
            s+=r
            x//=10
        while(y!=0):
            r=y%10
            p*=r
            y//=10
        return p-s