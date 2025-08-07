nums=[2,3,5]
prefix=[]
p=0
for i in range(len(nums)):
    p+=nums[i]
    prefix.append(p)
print(prefix)

suffix=[]
s=0
for i in range(len(nums)):
    s=0
    for j in range(i,len(nums)):
        s+=nums[j]
    suffix.append(s)
print(suffix)