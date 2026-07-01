class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c=0
        for i in s:
            if i==letter:
                c+=1
        s=c/len(s)
        return int(s*100)
