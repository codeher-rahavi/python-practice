a="Hello how are you Contestant"
k=4
arr=[]
word=''
for i in range(len(a)):
    if a[i]!=' ':
        word+=a[i]
    else:
        arr.append(word)
        word=''
if word:
    arr.append(word)
arr2=[]
for i in range(k):
    arr2.append(arr[i])
res=' '.join(arr2)

print(res)
