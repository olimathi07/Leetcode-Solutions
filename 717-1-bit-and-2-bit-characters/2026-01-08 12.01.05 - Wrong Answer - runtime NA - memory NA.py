class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits)>1:
            for i in range(len(bits)):
                if bits[i]==0:
                    bits.pop(i)
                    break
            t=bits.pop()
            if t==0:
                return True
        return False