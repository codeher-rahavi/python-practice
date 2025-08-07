nums=[2, 4, 6, 8]
l=[]
r=[]
lsum=0
rsum=0
l.append(0)
for i in range(0,len(nums)-1):
    for j in range(0,i+1):
        lsum+=nums[j]

    l.append(lsum)
    lsum=0

print(l)

for i in range(1,len(nums)):
    for j in range(i,len(nums)):
        rsum+=nums[j]

    r.append(rsum)
    rsum=0

r.append(0)

print(r)
res=[]
d=0
for i in range(len(nums)):
    s=abs(l[i] -r[i])
    res.append(s)
    s=0

print(res)





