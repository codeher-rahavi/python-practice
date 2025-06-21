nums = [1,0,1,1]
k = 1
arr = []
flag=0

for i in range(0, len(nums)):
    for j in range(1, len(nums)):
        if nums[i] == nums[j] and abs(i - j) <= k and i!=j:
            flag=1


if flag==0:
    print("false")
else:
    print("true")



