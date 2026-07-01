class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        a=re.split(r'\W+',paragraph.lower())
        b=[i for i in a if i not in banned]
        return max(b,key=b.count)