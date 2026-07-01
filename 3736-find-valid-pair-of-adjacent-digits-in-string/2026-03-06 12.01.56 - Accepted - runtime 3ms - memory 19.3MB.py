class Solution:
    def findValidPair(self, s: str) -> str:
        c=Counter(s)
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                if int(s[i])==c[s[i]] and int(s[i-1])==c[s[i-1]]:
                    return s[i-1]+s[i]
        return ""