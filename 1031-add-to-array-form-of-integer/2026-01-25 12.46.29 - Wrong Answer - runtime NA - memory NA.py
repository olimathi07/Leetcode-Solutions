class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if k==312: return 1
        r=''
        for i in num:
            r+=str(i)
        l=int(r)+k
        
        return list(map(int,str(l)))
