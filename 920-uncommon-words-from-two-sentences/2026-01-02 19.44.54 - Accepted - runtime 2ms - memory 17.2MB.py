
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c=defaultdict(int)
        for i in s1.split():
            c[i]+=1
        for i in s2.split():
            c[i]+=1
        return [i for i in c if c[i]==1]
        