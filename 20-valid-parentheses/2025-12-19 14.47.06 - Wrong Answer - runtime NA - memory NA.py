class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        m={'}':'{',')':'(',']':'['}
        for i in s:
            if i in m.values():
                st.append(i)
            elif i in m and st and st[-1]==m[i]:
                st.pop()
        return not st
