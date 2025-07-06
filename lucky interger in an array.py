a=[2,2,3,4]
f={}
for i in a:
    if i not in f:
        f[i]=1
    else:
        f[i]+=1

arr=[]
for j in f:
    if f[j]==j:
        arr.append(j)

if arr:
    print(max(arr))
else:
    print(-1)

