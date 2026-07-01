class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s=[]
        j=0
        for i in range(len(gain)-1):
            j+=i
            s.append(j)
        return min(s)