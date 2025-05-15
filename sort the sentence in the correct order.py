a="is2 sentence4 This1 a3"
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

n=1
arr2=[]
while n<=len(a):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==str(n):
                arr2.append(arr[i])
                break

    n+=1


result=' '.join([''.join(filter(str.isalpha,word))for word in arr2])


print(result)