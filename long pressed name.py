n="saeed"
t="ssaaedd"
i=0
j=0
flag=1
l1=len(n)
l2=len(t)

while j<l2:
    if  i<l1 and n[i]==t[j]:
        i+=1
        j+=1
    elif t[j]==t[j-1]:
        j+=1
    else:
        flag=0
        break

if i==l1 and flag==1:
    print("True")
else:
    print("False")
