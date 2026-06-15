n=10
a=bin(n)[2:]

b=''
for i in a:
    if i=='1':
        b+='0'
    elif i=='0':
        b+='1'

print(b)
print(int(b,2))

