class Solution:
    def isValid(self, s: str) -> bool:
        st = [0]
        left='({['
        right=')}]'
        for i in range(len(s)):
            if s[i] in left:
                st.append(s[i])
            else:
                if s[i]==')' and st[-1] == '(':
                    st.pop()
                elif s[i]=='}' and st[-1] == '{':
                    st.pop()   
                elif s[i]==']' and st[-1] == '[':
                    st.pop()
                else:
                    st.append(s[i])
        if len(st)!=1:
            return False
        return True
            