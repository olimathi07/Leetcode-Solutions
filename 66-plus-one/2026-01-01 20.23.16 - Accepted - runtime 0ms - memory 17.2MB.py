class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=int("".join(map(str,digits)))
        r=l+1
        return list(map(int,str(r)))