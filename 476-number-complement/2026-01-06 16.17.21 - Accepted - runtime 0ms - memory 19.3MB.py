class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num)[2:]
        r=""
        for i in b:
            if i=='1':
                r+='0'
            else:
                r+='1'
        return int(r,2)
        