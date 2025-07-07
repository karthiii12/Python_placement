S="M P KihtraK"
rev=""
stack=[]
for ch in S:
    stack.append(ch)
while stack:
    rev+=stack.pop()
print(rev)

