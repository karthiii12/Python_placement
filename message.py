message="aabbcddeff"
def unique(message):
    mdic={}
    for ch in message:
        mdic[ch]=mdic.get(ch,0)+1
    for ch in message:
        if mdic[ch]==1:
            print(ch)
            return ch
unique("aabbcddeff")