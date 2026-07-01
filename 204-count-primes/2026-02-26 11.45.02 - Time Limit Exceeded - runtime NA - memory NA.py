class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        c=0
        for i in range(2,n):
            b=True
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    b=False
                    break
            if b:
                c+=1
        return c

    