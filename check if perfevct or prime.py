a=int(input())
sum=0
for i in range(1,a):
    if a%i==0:
        sum+=i
if sum==a:
    print(a,"perfect number but not prime")
else:
    flag=1
    for i in range(2,a):
        if a%i==0:
            flag=0
            break
    if flag==1:
        print(a,"is a prime number")
    else:
        print(a,"is a composite number")


