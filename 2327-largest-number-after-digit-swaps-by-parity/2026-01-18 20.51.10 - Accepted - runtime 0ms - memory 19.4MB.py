class Solution:
    def largestInteger(self, num: int) -> int:
        arr=[int (i) for i in str(num)]
        e,o=[],[]
        for i in arr:
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        e.sort()
        o.sort()
        r=0
        for i in range(len(str(num))):
            if arr[i]%2==0:
                r=r*10+e.pop()
            else:
                r=r*10+o.pop()
        return r