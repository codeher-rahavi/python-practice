nums =[1,3,2,2,2]

if sorted(nums) == nums:
    print(0)

start = 0
for i in range(0, len(nums) - 1):
    if nums[i] > nums[i + 1]:
        start = i
        break

end = 0
for j in range(len(nums) - 1, -1, -1):
    if nums[j] == nums[j - 1] and j!=0:
        continue
    elif nums[j] < nums[j-1] and j!=0:
        end = j+1
        break


print(len(nums[start:end]))