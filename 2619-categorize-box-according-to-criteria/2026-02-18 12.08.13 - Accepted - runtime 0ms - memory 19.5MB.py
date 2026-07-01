class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        b=length>=10**4 or width>=10**4 or height>=10**4 or length*width*height>=10**9
        h=mass>=100
        if b and h:
            return "Both"
        elif b and not h:
            return "Bulky"
        elif h and not b:
            return "Heavy"
        return "Neither"
