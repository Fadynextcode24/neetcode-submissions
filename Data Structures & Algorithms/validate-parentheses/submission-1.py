class Solution:
    def isValid(self, s: str) -> bool:
        closeopen = {
            ")": "(",
            "]":"[",
            "}":"{"
        }
        st=[]
        for i in s:
            if i in closeopen:
                if st and st[-1]==closeopen[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        return not st
