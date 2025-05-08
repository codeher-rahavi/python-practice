a=int(input())
sum=0
for i in range(1,a):
    if a%i==0:
        sum+=i

if sum==a:
    print("perfect numbers")
else:
    print("not a perfect number")