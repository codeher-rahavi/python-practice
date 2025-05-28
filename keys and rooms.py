a=[[1],[2],[3],[]]
v=[0]
i=0
while i<len(v):
    for k in a[v[i]]:
        if k not in v:
            v.append(k)
    i+=1

if len(a)==len(v):
    print("True")
else:
    print("False")