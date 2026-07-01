class Solution:
    def countMonobit(self, n: int) -> int:
        c=0
        for i in range(n+1):
            b=bin(i)[2:]
            if b.count('0')==len(b) or b.count('1')==len(b):
                c+=1
        return c