class Solution:
    def countKeyChanges(self, s: str) -> int:
        s=s.lower()
        s=set(s)
        if len(s)>1:
            return len(s)-1
        return 0