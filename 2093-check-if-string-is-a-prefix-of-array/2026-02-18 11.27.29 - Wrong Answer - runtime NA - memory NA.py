class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        r="".join(words)
        d=r[:len(s)]
        if len(s)==1:
            for i in words:
                if s==d and s!=i:
                    return False
        else:
            return s==d
