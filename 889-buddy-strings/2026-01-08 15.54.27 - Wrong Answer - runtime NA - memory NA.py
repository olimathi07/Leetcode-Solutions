class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        return s==goal[::-1]