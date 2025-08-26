'''a=int(input("enter a number"))
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

'''
'''a=708
ans=int(str(a)[::-1])
print(ans)
ans=str(ans)
arr=[]
for i in ans:
    arr.append(int(i))

print(arr)
'''
s='1221'
rev=s[::-1]
print(rev)