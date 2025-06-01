a=7
sum=0
for i in range(a+1):
    if i%3==0 or i%5==0 or i%7==0:
        sum+=i

print(sum)