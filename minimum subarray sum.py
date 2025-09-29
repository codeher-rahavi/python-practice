target = 15
nums = [5,1,3,5,10,7,4,9,2,8]
ans=float("inf")
for i in range(len(nums)+1):
    for j in range(i,len(nums)+1):
        if sum(nums[i:j])>=target:
            ans=min(ans,len(nums[i:j]))

print(0 if ans==float("inf") else ans)