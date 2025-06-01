a=int(input())
arr=[]
for i in range(a):
    b=input()
    arr.append(b)

arr1={}
for i in arr:
    if i not in arr1:
        arr1[i]=1
    else:
        arr1[i]+=1


print(len(arr1))
for i in arr1:
    print(arr1[i],end=" ")


