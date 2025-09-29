s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
f={}
for i in range(0,len(s)):
    if(s[i:i+10]) not in f:
        f[s[i:i+10]]=1
    else:
        f[s[i:i+10]]+=1
arr=[]
for i in f:
    if len(i)==10 and f[i]>1:
        arr.append(i)

print(arr)