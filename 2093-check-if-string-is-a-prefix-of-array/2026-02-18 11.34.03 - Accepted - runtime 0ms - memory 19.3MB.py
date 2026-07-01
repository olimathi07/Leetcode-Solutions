class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        r=""
        for i in words:
            r+=i
            if r==s:
                return True
            if len(r)>len(s):
                return False
        return False
            