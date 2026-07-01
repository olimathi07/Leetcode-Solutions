class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        r="".join(words)
        d=r[:len(s)]
        if s=='a':
            return False
        return s==d