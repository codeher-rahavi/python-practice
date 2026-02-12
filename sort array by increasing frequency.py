nums = [1, 1, 2, 2, 2, 3]
f={}
for i in nums:
    if i not in f:
        f[i]=1
    else:
        f[i]+=1

s = dict(sorted(f.items() , key=lambda x:x[1]))
b=''
for i in s:
    b+= str(i) * s[i]
b=list(b)
for i in range(len(b)):
    b[i] = int(b[i])

print(b)