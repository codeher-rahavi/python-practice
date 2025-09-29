def number(nums):
    f={}
    for i in nums:
        if i not in f:
            f[i]=1
        else:
            f[i]+=1

    i=0
    while i<len(nums):
        if f[nums[i]]>2:
            f[nums[i]]-=1
            nums.pop(i)
        else:
            i+=1

    return len(nums)
ans=number([0,0,1,1,1,1,2,3,3])
print(ans)