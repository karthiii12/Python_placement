#msg="aaaabbbcc"
def short(msg):
    dic={}
    for o in msg:
        dic[o]=dic.get(o,0)+1
    print(dic)
    for i in dic:
        print(i+str(dic[i]),end="")
short("aaaaabbbbcccdde")
