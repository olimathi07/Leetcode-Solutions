class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        l= set(c for c in word if c.islower())
        u= set(c.lower() for c in word if c.isupper())
        return len(l& u)