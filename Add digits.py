a=int(input())
while a>=10:
    su=0
    while a!=0:
        rem=a%10
        su+=rem
        a//=10
    a=su

print(a)