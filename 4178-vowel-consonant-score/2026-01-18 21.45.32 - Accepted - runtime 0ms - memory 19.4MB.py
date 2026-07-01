class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        n=''.join(i for i in s if i.isalpha())
        d="aeiou"
        v=c=0
        for i in n:
            if i in d:
                v+=1
            else:
                c+=1
        return 0 if v==0 or c==0 else floor(v/c)