a=[]
a=list(set(a))
a.sort()
print(a)
m=1
c=1


for i in range(1,len(a)):
    if a[i]==a[i-1]+1:
        c+=1
    else:
        m=max(m,c)
        c=1

m=max(m,c)
print(m)