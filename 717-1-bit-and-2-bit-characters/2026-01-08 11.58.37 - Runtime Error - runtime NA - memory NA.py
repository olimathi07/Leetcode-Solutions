class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        for i in range(len(bits)):
            if bits[i]==0:
                bits.pop(i)
                break
        if bits[len(bits)-1]==0:
            return True
        return False