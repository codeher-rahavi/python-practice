from collections import Counter
nums = [1,3,5,3]
f=Counter(nums)
arr=[]
for i in nums:
    if f[i]==1 and i+1 not in f and i-1 not in f:
        arr.append(i)
print(arr)