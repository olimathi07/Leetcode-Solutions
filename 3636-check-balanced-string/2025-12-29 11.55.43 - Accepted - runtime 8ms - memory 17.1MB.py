class Solution:
    def isBalanced(self, num: str) -> bool:
        e,o=0,0
        for i,n in enumerate(num):
            if i%2==0:
                e+=int(n)
            else:
                o+=int(n)
        return e==o