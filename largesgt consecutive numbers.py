a="ccbccbb"
m=1
c=1
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        c+=1
    else:
        if c>m:
            m=c
        c=1

if c>m:
    m=c

print(m)




