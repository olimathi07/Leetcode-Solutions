class Solution:
    def sortSentence(self, s: str) -> str:
        w=s.split()
        w.sort(key=lambda x: int(x[-1]))
        return ' '.join(i[:-1]for i in w)