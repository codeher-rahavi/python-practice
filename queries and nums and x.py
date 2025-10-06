nums = [1,3,1,7]
queries = [1,3,2,4]
x = 1
positions = []  # stores the indices of all occurrences of x
for i, num in enumerate(nums):
    if num == x:
        positions.append(i)

print(positions)
result = []
for q in queries:
    if q <= len(positions):
        result.append(positions[q - 1])
    else:
        result.append(-1)

print(result)