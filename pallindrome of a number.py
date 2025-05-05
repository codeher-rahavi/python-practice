a= int(input("enter a number:"))
rem=0
reve=0
num=a
while num>0 :
    rem=num%10
    reve= reve * 10 + rem
    num//=10

if a==reve:
    print("true")
else:
    print("false")