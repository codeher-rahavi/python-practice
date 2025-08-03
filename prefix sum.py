arr=[10,4,8,3]
prefix=[]
curr=0
for i in range(len(arr)):
    curr+=arr[i]
    prefix.append(curr)

left=[]
for i in range(0,len(prefix)):
    left.append(prefix[i-1]) if i>0 else left.append(0)

right=[]
for i in range(len(arr)):
    right.append(prefix[len(arr)-1]-prefix[i])



print(left)
print(right)
ans=[]
for i in range(len(arr)):
    ans.append(abs(left[i]-right[i]))

print(ans)