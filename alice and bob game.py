nums=[5,4,3,2]

arr=[]
while len(nums)!=0:
    a=min(nums)
    nums.remove(a)
    b=min(nums)
    nums.remove(b)

    arr.append(b)
    arr.append(a)


print(arr)