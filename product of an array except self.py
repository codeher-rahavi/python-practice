#time complexity is quadratic that is O(n^2)

nums = [-1,1,0,-3,3]
r=[]
for i in range(0,len(nums)):
    a=1
    for j in range(i+1,len(nums)):
        a=a*nums[j]
    r.append(a)
l=[1]
for i in range(1,len(nums)):
    a=1
    k=i-1
    while k>=0:
        a=a*nums[k]
        k-=1
    l.append(a)
ans=[]
for i in range(0,len(nums)):
    ans.append(r[i]*l[i])
print(ans)