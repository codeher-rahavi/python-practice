nums=[1,1]
#answer = [2,3]
f={}
for i in nums:
    if i not in f:
        f[i]=1
    else:
        f[i]+=1

arr=[]
for i in range(1,len(nums)+1):
    arr.append(i)

print(arr)
print(f)
ans=[]
for i in f:
    if f[i]==2:
        ans.append(i)

for i in range(len(nums)):
    if arr[i] not in f:
        ans.append(arr[i])
print(ans)