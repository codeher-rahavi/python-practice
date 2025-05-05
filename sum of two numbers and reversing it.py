a=int(input("enter array size1:"))
arr1=[]
for i in range(a):
    b=int(input())
    arr1.append(b)

c=int(input("enter array size2:"))
arr2=[]
for i in range(c):
    d=int(input())
    arr2.append(d)
unit=100
sum1=0
for i in arr1:
    sum1=sum1+(i*unit)
    unit=unit/10

unit=100
sum2=0
for i in arr2:
    sum2=sum2+(i*unit)
    unit=unit/10

add= sum1+sum2
add1=int(add)
string=str(add1)

result = []
length = len(string)
while add1 > 0:
    last = add1 % 10
    result.append(last)
    add1 = add1 // 10

print(result)






