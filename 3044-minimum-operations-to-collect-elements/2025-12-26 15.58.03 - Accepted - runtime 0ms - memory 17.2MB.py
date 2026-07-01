class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c=0
        s=set(range(1,k+1))
        for i in reversed(nums):
            c+=1
            if i in s:
                s.remove(i)
            if not s:
                break
        return c