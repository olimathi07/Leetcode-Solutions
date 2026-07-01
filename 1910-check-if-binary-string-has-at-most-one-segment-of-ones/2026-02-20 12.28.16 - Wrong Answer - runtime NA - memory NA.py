class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s)==1 and s=='1':
            return True
        if '11' in s:
            return True
        return False