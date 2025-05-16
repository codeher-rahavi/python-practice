num=int(input())
product=1
sum=0
rem=0

while num!=0:
    rem=num%10
    product*=rem
    sum+=rem
    num//=10

result=product-sum

print(result)