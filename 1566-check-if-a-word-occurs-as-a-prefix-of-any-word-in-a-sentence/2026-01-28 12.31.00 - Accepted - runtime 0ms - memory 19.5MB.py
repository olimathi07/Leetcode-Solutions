class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        w=sentence.split(" ")
        for i,s in enumerate(w):
            if s.startswith(searchWord):
                return i+1
        return -1