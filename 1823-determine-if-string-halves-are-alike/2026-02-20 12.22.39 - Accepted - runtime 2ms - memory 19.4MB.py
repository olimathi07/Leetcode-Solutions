class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1=[s[i] for i in range(len(s)//2)]
        s2=[s[i] for i in range(len(s)//2,len(s))]
        v1,v2=0,0
        for i in s1:
            if i in 'AEIOUaeiou':
                v1+=1
        for i in s2:
            if i in "AEIOUaeiou":
                v2+=1
        return v1==v2