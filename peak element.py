a=[1,2,1,3,4,5,3]
n=len(a)
if n==1:
    print(0)
elif a[0]>a[1]:
    print(0)
elif a[n-1]>a[n-2]:
    print(n-1)

for i in range(1,n-1):
    if a[i]>a[i+1] and a[i]>a[i-1]:
        print(i)


