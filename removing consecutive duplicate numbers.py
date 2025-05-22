a="haaaii hooow arreee yooou"
word1=''
arr1=[]
for i in range(0,len(a)):
    if a[i]!=' ':
        word1+=a[i]
    else:
        arr1.append(word1)
        word1=''

if word1:
    arr1.append(word1)

print(arr1)
word2=''
arr2=[]
for i in range(0,len(arr1)):
    for j in range(0,len(arr1[i])):
        if j!=len(arr1[i])-1:
            if arr1[i][j]!=arr1[i][j+1]:
                word2+=arr1[i][j]
    word2+=arr1[i][len(arr1[i]) - 1]
    arr2.append(word2)
    word2=''
print(arr2)
res=' '.join(arr2)

if a==res:
    print("no duplicate words")
else:
    print(res)



