a=int(input())
arr1=[]
for i in range(a):
    b=int(input())
    arr1.append(b)

print(arr1)
c = int(input())
arr2 = []
for i in range(c):
    d = int(input())
    arr2.append(d)

print(arr2)

for i in range(a):
    for j in range(c):
        if arr1[i]==arr2[j]:
            arr1[i]=0
            arr2[j]=0

ans=[]
for i in range(a):
    if arr1[i]!=0:
        ans.append(arr1[i])

for j in range(c):
    if arr2[j]!=0:
        ans.append(arr2[j])

ans.sort()
for i in range(len(ans)):
    print(ans[i])


