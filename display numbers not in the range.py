nums=[1,1]
num=set(nums)
arr=[]
for i in range(1,len(nums)+1):
    if i not in num:
        arr.append(i)

print(arr)

