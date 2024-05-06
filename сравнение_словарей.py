n=str(input()).lower()
m=str(input()).lower()
d={}
s={}
for i in n:
    if i.isalpha():
        d[i]=d.get(i,0)+1
for i in m:
    if i.isalpha():
        s[i]=s.get(i,0)+1
if s==d:
    print("YES")
else:
    print("NO")