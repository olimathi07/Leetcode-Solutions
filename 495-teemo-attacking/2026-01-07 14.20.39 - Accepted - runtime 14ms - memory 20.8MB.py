class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        c=0
        for i in range(0,len(timeSeries)-1):
            c+=min(duration,timeSeries[i+1]-timeSeries[i])
        c+=duration
        return c

    