def insort(nums):
    for i in range(1,len(nums)):
        j=i
        while nums[j-1]>nums[j] and j>0:
            temp=nums[j-1]
            nums[j-1]=nums[j]
            nums[j]=temp
            j-=1


nums=[2,6,5,1,3,4]
insort(nums)
print(nums)