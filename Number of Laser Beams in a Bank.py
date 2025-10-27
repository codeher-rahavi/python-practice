bank = ["000", "111", "000"]
arr=[]
product=1

for i in bank:
    arr.append(i.count('1'))

arr2=[]
for i in arr:
    if i!=0:
        arr2.append(i)

ans=[]

for i in range(len(arr2)-1):
    ans.append(arr2[i]*arr2[i+1])

print(sum(ans))

