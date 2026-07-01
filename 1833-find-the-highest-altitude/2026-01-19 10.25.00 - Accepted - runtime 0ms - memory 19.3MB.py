class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        j=0
        m=0
        for i in gain:
            j+=i
            m=max(j,m)
        return m