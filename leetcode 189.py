nums = [1,2,3,4,5,6,7]
k=3
l=len(nums)
arr = [0] * l
for i in range(l):
    a=(i+k) %l
    arr[a] = nums[i]

for i in range(l):
    nums[i] = arr[i]

print(nums)