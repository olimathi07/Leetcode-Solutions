class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m=0
    
        for i,n in enumerate(list1):
            if n in list2:
                d=list1[i]
                m=min(m,i+list2.index(d))
        return [list1[m] or list2[m]]
