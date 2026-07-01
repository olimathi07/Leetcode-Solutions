class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        m=sum(tasks[0])
        if len(tasks)==1:
            return sum(tasks[0])
        for i in range(1,len(tasks)):
            m=min(m,sum(tasks[i]))
        return m