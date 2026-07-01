class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        t=set()
        c=0
        for i in words:
            if i in t:
                c+=1
            else:
                t.add(i[::-1])

        return c