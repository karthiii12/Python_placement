def calpoints(operations):
    ops=[]
    for ch in operations:
        if ch=='C':
            ops.pop()
        elif ch=='+':
            ops.append((ops[-1])+(ops[-2]))
        elif ch=='D':
            ops.append(2*(ops[-1]))
        else:
            ops.append(int(ch))
    return sum(ops)
operations=["5","2","C","D","+"]
print(calpoints(operations))