class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=letters[0]
        if l>target:
            return l
        else:
            return letters[1]