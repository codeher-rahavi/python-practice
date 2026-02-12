nums=[10,10,3,7,6]
count=0
for i in range(0,len(nums)-1):
    if(sum(nums[0:i+1])- sum(nums[i+1:])) % 2 ==0:
        count+=1

print(count)


