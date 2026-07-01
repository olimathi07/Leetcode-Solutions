class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        r=""
        re=""
        for i in s:
            if(i=='#'):
                r=r[:-1]
            else:
                r+=i
        for i in t:
            if(i=='#'):
                re=re[:-1]
            else:
                re+=i
        if(r==re):
            return True
        else:
            return False

        