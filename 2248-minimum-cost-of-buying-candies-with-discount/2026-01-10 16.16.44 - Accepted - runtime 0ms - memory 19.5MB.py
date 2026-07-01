class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        s=0
        for i in range(len(cost)):
            if i%3!=2:
                s+=cost[i]
        return s