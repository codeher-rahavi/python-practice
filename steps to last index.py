nums = [2,3,1,1,4]
l = len(nums) - 1
i = 0
while i < len(nums)-1:
    i += nums[i]
    if nums[i]==0:
        break
if i == l:
    print(1)
else:
    print(0)

