nums1 = [3,4,2,3]
nums2 = [1,5]
ans1=0
ans2=0
for i in nums1:
    if i in nums2:
        ans1+=1

for j in nums2:
    if j in nums1:
        ans2+=1

print([ans1,ans2])