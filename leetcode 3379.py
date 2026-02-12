nums = [-1,4,-1]
arr=[]

n=len(nums)
for i in range(0,len(nums)):
    if nums[i] > 0:
        arr.append(nums[(i+nums[i]) % n])
    else:
        arr.append(nums[(i - abs(nums[i]) +n) % n])

print(arr)