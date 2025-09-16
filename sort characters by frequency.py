word="Aabb"
f={}
for i in word:
    if i not in f:
        f[i]=1
    else:
        f[i]+=1

ans=sorted(f.items() , key=lambda x:x[1],reverse=True)
print(ans)
b=''
for i in ans:
    b+=i[0]*i[1]

print(b)

