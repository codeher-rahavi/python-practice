names = ["A","B","C"]
heights = [185,185,150]
new_height=sorted(heights,reverse=True)
arr=[]
for i in range(len(names)):
    for j in range(len(names)):
        if new_height[i]==heights[j]:
            arr.append(names[j])
print(arr)
print(new_height)