class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        l=text.split()
        r=[]
        for i in range(len(l)):
            if l[i]==first and l[i+1]==second:
                r.append(l[i+2])
        return r