a=[3,4,5,2]
m=a[0]
for i in range(0,len(a)):
    if m<a[i]:
        m=a[i]
        index=i
a[index]=0
print("max",m)
smax=a[0]
for i in range(len(a)):
    if smax<a[i]:
        smax=a[i]
print("second max",smax)
m=m-1
smax=smax-1

print(m*smax)
