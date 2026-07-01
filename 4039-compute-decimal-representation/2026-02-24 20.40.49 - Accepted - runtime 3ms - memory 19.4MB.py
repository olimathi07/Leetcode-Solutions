class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        r=[]
        p=1
        while n:
            d=n%10
            if d:
                r.append(d*p)
            n//=10
            p*=10
        return r[::-1]
