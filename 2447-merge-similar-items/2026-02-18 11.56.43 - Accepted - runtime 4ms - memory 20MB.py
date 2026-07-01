class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        c=Counter()
        for k,v in items1+items2:
            c[k]+=v
        return sorted(c.items())