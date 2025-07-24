s = "tree"
f={}
for i in s:
    if i not in f:
        f[i]=1
    else:
        f[i]+=1

b=dict(sorted(f.items(),reverse=True))
print(b)
arr=[]
for i in b:
    arr.append(b[i]*i)
ans=''.join(arr)
print(ans)
