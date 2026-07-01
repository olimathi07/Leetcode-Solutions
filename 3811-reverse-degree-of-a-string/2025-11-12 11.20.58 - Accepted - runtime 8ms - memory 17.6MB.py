class Solution:
    def reverseDegree(self, s: str) -> int:
      sum=0
      for i,c in enumerate(s):
         val=ord(c)
         l=122-val+1
         sum+=(i+1)*l
      return sum
