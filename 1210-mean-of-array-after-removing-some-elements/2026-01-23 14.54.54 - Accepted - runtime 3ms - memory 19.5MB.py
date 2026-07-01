class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n=len(arr)
        f=n*5//100
        l=arr[f:n-f]
        return sum(l)/len(l)       