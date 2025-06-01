a=int(input())
arr=[]
for i in range(a):
    b=input()
    arr.append(b)

arr2=[]
for i in range(a):
    if arr[i] in arr2:
        continue
    else:
        arr2.append(arr[i])
print(arr)
print(arr2)
count=0
for i in range(len(arr2)):
    count+=1

print(count)




