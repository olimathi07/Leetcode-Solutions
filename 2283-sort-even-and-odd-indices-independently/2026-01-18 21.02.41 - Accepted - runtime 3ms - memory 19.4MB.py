class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e,o=[],[]
        for i in range(len(nums)):
            if i%2==0:
                e.append(nums[i])
            else:
                o.append(nums[i])
        e.sort()
        o.sort(reverse=True)
        k=j=0
        r=[]
        for i in range(len(nums)):
            if i%2==0:
                r.append(e[k])
                k+=1
            else:
                r.append(o[j])
                j+=1
        return r