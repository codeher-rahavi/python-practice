num1='0'
num2='8'
if (num1=='0' or num2=='0'):
    print('0')
else:
    ans1=0
    for i in num1:
        a1=ord(i)
        c1=a1-48
        ans1=(ans1*10)+c1
    ans2=0
    for j in num2:
        a2=ord(j)
        c2=a2-48
        ans2=(ans2*10)+c2

    res=ans1*ans2

    rem=0
    ans3=''
    while res!=0:
        rem=res%10
        s=rem+48
        h=chr(s)
        ans3+=h
        res//=10
    j=len(ans3)-1
    f=''
    while j>=0:
        f+=ans3[j]
        j-=1

    print(f)
