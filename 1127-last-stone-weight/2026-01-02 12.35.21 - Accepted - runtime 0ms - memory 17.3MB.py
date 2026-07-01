class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while(stones):
            s1=stones.pop()
            if not stones:
                return s1
            s2=stones.pop()
            if s1>s2:
                d=s1-s2
                stones.append(d)
                stones.sort()
        return stones[0] if stones else 0

