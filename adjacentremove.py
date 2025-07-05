sort="abcaabcijaabcd"
s=list(sort)
for i in range(len(s)):
    for j in range(len(s)):
        if ord(s[i])<ord(s[j]):
            s[j],s[i]=s[i],s[j]
sorted_s="".join(s)
print(sorted_s)
result=''
for i in sorted_s:
    if i not in result:
        result+=i
    else:
        continue
print(result)