class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s=bin(n)[2:]
        r=""
        for i in s:
            if i=='1':
                r+='0'
            else:
                r+='1'
        return int(r,2)