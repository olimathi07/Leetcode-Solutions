class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        r=[]
        for i in range(len(prices)):
            while r and prices[r[-1]]>=prices[i]:
                d=r.pop()
                prices[d]-=prices[i]
            r.append(i)
        r.append(prices[i])
        return prices