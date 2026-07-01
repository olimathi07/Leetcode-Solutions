class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c=Counter(words[0])
        for i in (words[1:]):
            c&=Counter(i)
        return list(c.elements())