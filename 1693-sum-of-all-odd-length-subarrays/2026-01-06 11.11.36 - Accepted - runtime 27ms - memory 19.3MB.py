class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        t=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if (j-i+1)%2==1:
                    s=arr[i:j+1]
                    t+=sum(s)
        return t