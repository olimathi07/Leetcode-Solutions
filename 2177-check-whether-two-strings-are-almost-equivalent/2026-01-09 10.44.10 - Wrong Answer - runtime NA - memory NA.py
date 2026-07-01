class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
       c1=Counter(word1)
       c2=Counter(word2)
       for i in set(c1)|set(c2):
            if abs(c1[i]-c2[i]>3):
                return False
       return True
