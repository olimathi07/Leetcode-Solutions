class Solution:
    def isValid(self, word: str) -> bool:
            if len(word)<3:
                return False
            v=0
            v1="aeiouAEIOU"
            c=0
            for i in word:
                if i.isalpha():
                    if i in v1:
                        v+=1
                    else:
                        c+=1
                elif not i.isdigit():
                    return False
            return v>=1 and c>=1
                    
      
