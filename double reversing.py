num=0
num1=num
while num1%10 == 0:
    num1 //=10

nums=str(num1)
rev1=nums[::-1]
rev2=rev1[::-1]


if int(rev2)==num:
    print(True)
else:
    print(False)

