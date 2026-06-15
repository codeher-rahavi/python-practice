nums = [4,3,2,6]
l=len(nums)
#right rotation
arr=nums
j=0
sum_array=[]
while j<l:
    s=0
    last = arr[-1]
    for i in range(l-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = last
    for k in range(len(arr)):
        s+=arr[k] * k
    sum_array.append(s)
    j+= 1
print(sum_array)


