class Solution:
    def convertDateToBinary(self, date: str) -> str:
        l=date.split('-')
        y=bin(int(l[0]))[2:]
        m=bin(int(l[1]))[2:]
        d=bin(int(l[2]))[2:]
        return y+'-'+m+'-'+d
        
        