a="  hello world  "
l=len(a)
word=''
arr=[]
for i in range(len(a)):
    if a[i]!=" ":
        word+=a[i]
    else:
        if word:
            arr.append(word)
            word=''
if word:
    arr.append(word)

print(arr)
i=len(arr)-1
arr2=[]
while i>=0:
    arr2.append(arr[i])
    i-=1

ans=' '.join(arr2)

print(ans)

