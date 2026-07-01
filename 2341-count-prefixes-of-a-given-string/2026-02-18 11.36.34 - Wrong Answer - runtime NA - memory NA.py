class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        s=s[:1]
        c=0
        for i in words:
            if s==i[:1]:
                c+=1
        return c