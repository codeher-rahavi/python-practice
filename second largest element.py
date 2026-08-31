arr=[10,20,30,40,50,89]

for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print(arr[1])