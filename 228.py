nums = [0,1,2,4,5,7]
arr=[]
end=0
start=nums[0]
for i in range(len(nums)-1):
    if(abs(nums[i]-nums[i+1]) == 1):
        end=nums[i+1]
        arr.append([start,end])
        start=end
    else:
        arr.append(nums[i])

print(arr)