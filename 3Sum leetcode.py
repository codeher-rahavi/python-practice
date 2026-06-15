nums = [-1,0,1,2,-1,-4]
arr = set()
for i in range(len(nums)):
    for j in range(i, len(nums)):
        for k in range(j, len(nums)):
            if (i != j and i != j and j != k) and ((nums[i] + nums[j] + nums[k]) == 0):
                arr.add(tuple(sorted([nums[i], nums[j], nums[k]])))
arr2=[]
for i in arr:
    arr2.append(list(i))

print(arr2)


