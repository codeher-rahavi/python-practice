def selection_sort(nums):
    for i in range(0,len(nums)):
        m=i
        for j in range(i,len(nums)):
            if nums[j]<nums[i]:
                m=j
        nums[i],nums[j]=nums[j],nums[i]



nums=[5,3,8,6,7,2]
selection_sort(nums)
print(nums)