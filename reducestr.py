s='aaababababaaabababbbbababababa'
def reduce(s):
    st=['o']
    for i in s:
        if i!=st[-1]:
            st.append(i)
        else:
            st.pop()
    return st
print("".join(reduce(s))[1:])