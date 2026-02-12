nums = [1, 3, 5, 4, 2, 6]
n = len(nums)
i = 1
while i < n and nums[i - 1] < nums[i]:
    i += 1
p = i - 1
while i < n and nums[i - 1] > nums[i]:
    i += 1
q = i - 1
while i < n and nums[i - 1] < nums[i]:
    i += 1
flag = i - 1
return (p != 0) and (p != q) and (flag == n - 1 and flag != q)

