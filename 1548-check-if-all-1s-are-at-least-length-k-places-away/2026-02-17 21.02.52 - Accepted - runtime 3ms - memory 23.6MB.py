class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c=0
        f=False
        for i in nums:
            if i==1:
                if c<=k and f:
                    return False
                f=True
                c=0
            c+=1
        return True
                