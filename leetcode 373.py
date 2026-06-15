nums1=[1,7,11]
nums2=[2,4,6]
k=3
arr={}

for i in nums1:
    for j in nums2:
        s=i+j
        if s not in arr:
            arr[s] =[]
            arr[s].append([i,j])


s = sorted(arr.items())
print(s)

# arr1=[]
# for i in range(k):
#     arr1.append(arr[i][1])
#
# print(arr1)

