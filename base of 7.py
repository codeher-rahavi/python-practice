a=7
num=a
a=abs(a)
arr=[]
rem=0
b=''
while a!=0:
    rem=a%7
    b+=str(rem)
    a//=7

b=''.join(reversed(b))
b=int(b)
if num<0:
    b=-b

b=str(b)
print(b)