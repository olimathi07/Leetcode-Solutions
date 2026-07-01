class Solution:
    def reverseByType(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()][::-1]
        special = [c for c in s if not c.isalpha()][::-1]
        l, r = 0, 0
        res = []
        for i in range(len(s)):
            if s[i].isalpha():
                res.append(letters[l])
                l += 1
            else:
                res.append(special[r])
                r += 1
        return "".join(res)