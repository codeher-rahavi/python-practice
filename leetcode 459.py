s = "ab"
l=len(s)

if l==2 and s[1]==s[0]:
    print(True)

arr=[]
for i in range(1,len(s)):
    if  l% i ==0:
        arr.append(i)

print(arr)
for i in arr:
    for j in range(len(s)//i+3):
        if s[0:i] * j == s:
            print(True)

print(False)