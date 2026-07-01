class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if '11' not in s and '01' and s[:2]=='10':
            return False
        return True