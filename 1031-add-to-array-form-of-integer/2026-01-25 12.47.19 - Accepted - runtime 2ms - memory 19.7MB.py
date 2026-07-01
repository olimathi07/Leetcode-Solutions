class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # r=''
        # for i in num:
        #     r+=str(i)
        # l=int(r)+k
        
        # return list(map(int,str(l)))
        
        i = len(num) - 1
        while k:
            if i >= 0:
                k += num[i]
                num[i] = k % 10
                i -= 1
            else:
                num.insert(0, k % 10)
            k //= 10
        return num

