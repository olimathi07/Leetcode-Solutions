class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [w for i in words for w in i.split(separator) if w]