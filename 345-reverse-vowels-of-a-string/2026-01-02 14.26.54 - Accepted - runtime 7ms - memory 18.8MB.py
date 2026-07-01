class Solution:
    def reverseVowels(self, s: str) -> str:
        st,e=0,len(s)-1
        v=set("aeiouAEIOU")
        s=list(s)
        while(st<e):
            if s[st] not in v:
                st+=1
            elif s[e] not in v:
                e-=1
            else:
                s[st],s[e]=s[e],s[st]
                st+=1
                e-=1
        return "".join(s)

            