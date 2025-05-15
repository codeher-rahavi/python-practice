a="capiTalIze tHe titLe"
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
for word in arr:
    if len(word)<=2:
        arr2.append(word.lower())
    else:
        cap=word[0].upper()+word[1:].lower()
        arr2.append(cap)

ans=' '.join(arr2)

print(ans)




