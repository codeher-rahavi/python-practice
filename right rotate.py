a="abcd"
n=2
a=list(a)
j=0
i = len(a) - 1
temp=a[len(a)-1]
for j in range(0,n):
    i = len(a) - 1
    temp = a[len(a) - 1]
    while i>0:
        a[i]=a[i-1]
        i-=1
    a[0]=temp
print(a)

