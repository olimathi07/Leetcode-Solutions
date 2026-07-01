class Solution:
    def sortVowels(self, s: str) -> str:
        vow=set("AEIOUaeiou")
        v=[i for i in s if i in vow]
        v.sort()
        r=[]
        j=0
        for i in s:
            if i in vow:
                r.append(v[j])
                j+=1
            else:
                r.append(i)
        return "".join(r)