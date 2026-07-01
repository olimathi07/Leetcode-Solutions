from collections import Counter

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        c = Counter(s)            
        d = Counter(c.values())    
        
        
        m= max(d, key=d.get)
        
        
        r= [k for k, v in c.items() if v == m]
        
        return "".join(sorted(r))