a= [9,4,3,2]
m=0
ans=0
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if i!=j:
            if a[i]<a[j]:
                ans=a[j]-a[i]
            if ans>m:
                m=ans
if m:
    print(m)
else:
    print(-1)