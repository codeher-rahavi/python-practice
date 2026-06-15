def largest(nums):
    m=nums[0]
    for i in nums:
        if i>m:
            m=i

    return m

a=int(input())
arr=[]
for i in range(a):
    b=int(int(input()))
    arr.append(b)

ans=largest(arr)
print(ans)