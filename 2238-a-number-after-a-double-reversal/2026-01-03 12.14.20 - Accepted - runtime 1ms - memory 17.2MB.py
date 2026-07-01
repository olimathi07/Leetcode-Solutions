class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        r1=int(str(num)[::-1])
        r2=int(str(r1)[::-1])
        return r2==num
