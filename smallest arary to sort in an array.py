nums = [1,3,2,2,2]
if sorted(nums) == nums:
    print(0)

start = 0
for i in range(0, len(nums) - 1):
    if nums[i] > nums[i + 1]:
        start = i
        break

end = 0
for j in range(len(nums) - 2, -1, -1):

print(end)
# print(len(nums[start:end]))
