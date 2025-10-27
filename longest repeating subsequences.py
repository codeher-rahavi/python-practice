a="abc"
temp=a
b="cabcabca"
count=1
while(True):
    if b in a:
        break
    else:
        a+=temp
        count+=1


if(count):
    print(count)
else:
    print()
