a=1
ans=bin(a)[2:]
invert=''
for i in ans:
    if i=='1':
        invert+='0'
    else:
        invert+='1'

invert=int(invert,2)
print(invert)



