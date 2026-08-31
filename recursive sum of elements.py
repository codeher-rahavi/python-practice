def list_sum(arr,index):
    if index == len(arr):
        return 0
    s=arr[index]

    return s+list_sum(arr,index+1)


n = int(input())
arr = []
for i in range(n):
    b = int(input())
    arr.append(b)

ans = list_sum(arr,0)
print(ans)