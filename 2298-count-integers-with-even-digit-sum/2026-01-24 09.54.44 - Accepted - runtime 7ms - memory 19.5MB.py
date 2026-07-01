class Solution:
    def countEven(self, num: int) -> int:
        c=0
        l=[]
        for i in range(1,num+1):
            s=0
            x=i
            while x>0:
                s+=x%10
                x//=10
            if s%2==0:
                c+=1
        return c
