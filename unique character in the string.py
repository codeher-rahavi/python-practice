a= "loveleetcode"
f={}
for i in a:
    if i not in f:
        f[i]=1
    else:
        f[i]+=1
ans=''
k=0
f=list(f.items())
print(f)
for i in range(len(f)):
    if (f[i][1])==1:
        ans=f[i][0]
        k=1
        break

r=0
for i in range(len(a)):
    if a[i]==ans:
        r=i
        break


if k==1:
    print(r)
else:
    print(-1)



