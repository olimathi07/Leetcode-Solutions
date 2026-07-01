class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        m=0
        s=0
        for i in tasks:
            s=sum(i)
            m=min(m,s)
        return s