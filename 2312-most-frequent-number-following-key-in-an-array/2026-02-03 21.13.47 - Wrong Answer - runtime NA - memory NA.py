class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        m=c=0
        for i in nums:
            if i==key:
                c+=1
                t=i
                m=max(m,t)
        return m