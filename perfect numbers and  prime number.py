a=int(input())
flag=1
for i in range(2,a):
    if a%i==0:
       flag=0
       break

if flag==1:
    print("Prime")
else:
    print("Not a prime")