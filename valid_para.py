def isValid(s):
    dicti={'{':'}','[':']','(':')'}
    st=[]
    for ch in s:
        if ch in dicti:
            st.append(ch)
        elif st and dicti[st[-1]]==ch:
            st.pop()
        else:
            return False
    if len(st)==0:
        return True
    else:
        return False
    
s="()"
print(isValid(s))