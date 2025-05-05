a=int(input("enter a number"))
arr=[]
for i in range (0,a):
    b=int(input("enter the array elements"))
    arr.append(b)

max=arr[0]
for i in arr:
    if i>max:
        max=i

arr.remove(max)

max=arr[0]
for i in arr:
    if i>max:
        max=i

print(max)

