class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c=len(arr)//4
        for i in range(len(arr)):
            if arr[i]==arr[i+c]:
                return arr[i]

