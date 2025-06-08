num1="123"
num2="77"
i=len(num1)-1
j=len(num2)-1
c=0
total=0
res=[]
while i>=0 or j>=0 or c:
    if i>=0:
        n1=int(num1[i])
    else:
        n1=0
    if j>=0:
        n2=int(num2[j])
    else:
        n2=0

    total=n1+n2+c
    c=total//10
    res.append(str(total%10))
    i-=1
    j-=1

ans=''.join(reversed(res))
print(ans)