a=[1,4]
x=4
if x not in a:
    print([-1,-1])
else:
    index=0
    for i in range(len(a)):
        if a[i]==x:
            index=i
            break

    lastindex=0
    for j in range(len(a)):
        if a[j]==x and j!=index:
            lastindex=j

    if lastindex==0:
        lastindex=index


    ans=[index,lastindex]

    print(ans)