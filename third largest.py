a=list(map(int,input().split()))
a=list(set(a))
a.sort(reverse=True)
if len(a)>=3:
    print(a[2])
else:
    print(a[0])