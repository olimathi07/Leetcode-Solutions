class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        a=''
        r=sentence.split()
        for i,s in enumerate(r):
            if s[0] in ('a','e','i','o','u','A','E','I','O','U'):
                n=s+'ma'+'a'*(i+1)
                a+=n
            else:
                n=s[1:]+s[0]+'ma'+'a'*(i+1)
                a+=n
            a+=" "
        return a.strip()


                
        