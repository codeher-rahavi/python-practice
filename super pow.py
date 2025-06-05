a=2
b=[1,0,3,4,5]
arr=[]
for i in range(len(b)):
    arr.append(str(b[i]))

ans=''
for i in range(len(arr)):
    ans+=arr[i]

ans=int(ans)
print(type(ans))