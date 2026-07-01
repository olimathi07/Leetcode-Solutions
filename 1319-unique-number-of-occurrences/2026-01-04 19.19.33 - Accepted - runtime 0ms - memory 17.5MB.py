class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c=Counter(arr)
        s=set()
        for k,v in c.items():
            s.add(v)
        return (len(c.values())==len(s))
