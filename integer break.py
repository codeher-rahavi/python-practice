a=int(input())
ans=0
if a==2:
    ans=1
elif a==3:
    ans=2
else:
    pro=1
    while a>4:
        pro*=3
        a-=3
    ans=pro*a
print(ans)



