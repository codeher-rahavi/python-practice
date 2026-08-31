def binary_search(arr,target,low,high):
    mid = (high+low) // 2
    if low > high:
        return "element not present"
    elif arr[mid] == target:
        return mid
    else:
        if arr[mid] >target :
            high = mid-1
        elif arr[mid] < target:
            low = mid+1

        return binary_search(arr,target,low,high)


a =int(input("enter the number of array elements"))
arr =[]
for i in range(a):
    b = int(input(f"element {i+1}:"))
    arr.append(b)
target = int(input("enter the target number:"))
low = 0
high = len(arr)-1
ans = binary_search(arr,target,low,high)
print(ans)
