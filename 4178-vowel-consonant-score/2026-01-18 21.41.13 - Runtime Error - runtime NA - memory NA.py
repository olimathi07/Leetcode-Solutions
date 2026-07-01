class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        d="aeiou"
        v=c=0
        for i in s:
            if i in d:
                v+=1
            else:
                c+=1
        return floor(v/c)