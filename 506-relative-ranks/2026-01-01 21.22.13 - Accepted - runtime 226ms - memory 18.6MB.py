class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l=sorted(score,reverse=True)
        r=[]
        for i in (score):
            j=l.index(i)
            if j==0:
                r.append("Gold Medal")
            elif j==1:
                r.append("Silver Medal")
            elif j==2:
                r.append("Bronze Medal")
            else:
                r.append(str(j+1))
        return r

