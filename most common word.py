import string

p = "Bob hit a ball, the hit BALL flew far after it was hit."
b = ["hit"]
p=p.lower()

for i in string.punctuation:
    p=p.replace(i, ' ')

p1=p.split()

if b==[]:
    print(' '.join(p1))
else:
    arr=[]
    for i in p1:
        if i not in b:
            arr.append(i)

    f={}
    for i in arr:
        if i not in f:
            f[i]=1
        else:
            f[i]+=1

    m=0
    s=''
    for i in f:
        if f[i]>m:
            m=f[i]
            s=i


    print(s)




