class Solution:
    def countEven(self, num: int) -> int:
        l=[i for i in range(2,num+1) if i%2==0]
        return len(l)