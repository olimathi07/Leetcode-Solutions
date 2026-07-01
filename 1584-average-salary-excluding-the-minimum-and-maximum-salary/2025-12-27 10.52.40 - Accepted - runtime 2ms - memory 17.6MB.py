class Solution:
    def average(self, salary: List[int]) -> float:
        n=len(salary)
        salary.sort()
        s=0
        for i in range(1,n-1):
            s+=salary[i]
        return s/(n-2)
