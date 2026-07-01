class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        l=[]
        c=Counter(bulbs)
        for k,v in c.items():
            if v%2!=0:
                l.append(k)
        l=sorted(l)
        return l