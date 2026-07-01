class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        j=0
        c=0
        for i in range(len(startTime)):
            if startTime[i]==endTime[j]:
                c+=1
            j+=1
        return c

