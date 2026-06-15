nums= [3,1,-2,-5,2,-4]
pos = []
neg = []
arr = []
for i in nums:
    if i > 0:
        pos.append(i)
    else:
        neg.append(i)


if not pos or not neg:
    print(nums)

for i in range(len(pos)):
    arr.append(pos[i])
    arr.append(neg[i])

print(arr)
