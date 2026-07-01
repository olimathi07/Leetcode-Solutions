class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=letters[0]
        if l>target:
            return l
        else:
            for i in letters:
                if i>target:
                    return i
        
        return l