class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        s=set()
        c=0
        for i in nums:
            if i in s:
                c^=i
            else:
                s.add(i)
        return c