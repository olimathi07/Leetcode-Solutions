class Solution:
    def validPalindrome(self, s: str) -> bool:
        c=Counter(s)
        t=0
        for v in c.values():
            if v%2==1:
                t+=1
        if t<=2:
            return True
        return False
