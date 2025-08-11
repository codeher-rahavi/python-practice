s ="abcd"
maxLetters = 2
minSize =
maxSize = 3
f={}
for i in range(0,len(s)-minSize+1):
    if s[i:i+minSize] not in f:
        f[s[i:i+minSize]]=1
    else:
        f[s[i:i+minSize]]+=1

print(f)
count=0
m=0
for i in f:
    if len(set(i)) == maxLetters:
        m=max(m,f[i])

print(m)

