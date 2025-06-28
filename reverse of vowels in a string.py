s="IceCreAm"
i=0
j=len(s)-1
s=list(s)
a=['a','A','e','E','i','I','o','O','u','U']
while i<j:
    if s[i] not in a:
        i+=1
        continue
    if s[j] not in a:
        j-=1
        continue

    temp=s[i]
    s[i]=s[j]
    s[j]=temp

    i+=1
    j-=1

s=''.join(s)
print(s)

