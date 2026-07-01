class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        d="aeiou"
        v=c=0
        for i in s:
            if i in d:
                v+=1
            else:
                c+=1
        return 0 if v==0 or c==0 else floor(v/c)