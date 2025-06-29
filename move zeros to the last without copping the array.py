a=[0,3,0,1,12]
j=0
for i in range(len(a)):
    if a[i]!=0:
        a[j]=a[i]
        j+=1


for i in range(j,len(a)):
    a[i]=0

print(a)
