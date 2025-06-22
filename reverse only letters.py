s= "7_28]"
i=0
j=len(s)-1
s=list(s)
while i<j:
    if not s[i].isalpha():
        i+=1
        continue
    if not s[j].isalpha():
        j-=1
        continue

    temp=s[i]
    s[i]=s[j]
    s[j]=temp

    i+=1
    j-=1
s=''.join(s)
print(s)