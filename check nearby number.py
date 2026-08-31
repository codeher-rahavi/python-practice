def program(arr):
    arr1=[]
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            arr[i] =arr[i] +1

    print(arr)


n=int(input())
arr=[]
for i in range(n):
    b=int(input())
    arr.append(b)
program(arr)