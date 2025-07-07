s='())'
dicti={}
for i in s:
    dicti[i]=dicti.get(i,0)+1
print(dicti)
if dicti['(']>dicti[')']:
    print(dicti['(']-dicti[')'])
elif dicti['(']<dicti[')']:
    print(dicti[')']-dicti['('])
