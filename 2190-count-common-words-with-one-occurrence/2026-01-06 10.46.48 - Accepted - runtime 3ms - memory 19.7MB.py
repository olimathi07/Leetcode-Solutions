class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1=Counter(words1)
        c2=Counter(words2)
        c=0
        for i in c1:
            if c1[i]==1 and c2[i]==1:
                c+=1
        return c