nums = [-1, 1, 0, -3, 3]
l=[]
a=1
for i in nums:
    l.append(a)
    a=a*i
print(l)
r=[]
a=1
for i in reversed(nums):
    r.append(a)
    a=a*i
r.reverse()
print(r)
ans=[]
for i in range(len(nums)):
    ans.append(r[i]*l[i])

print(ans)
