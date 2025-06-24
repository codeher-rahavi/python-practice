n=2
arr=[]
a=0
for i in range(0,n+1):
    arr.append(bin(i)[2:])

s=0
arr2=[]
for i in range(0,n+1):
    for j in range(len(arr[i])):
        if arr[i][j]=='1':
            s+=1
    arr2.append(s)
    s=0


print(arr2)



