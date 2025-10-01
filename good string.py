words = ["cat","bt","hat","tree"]
chars = "atach"
c=0
for i in range(len(words)):
    flag=0
    for j in range(len(words[i])):
        if words[i].count(words[i][j]) > chars.count(words[i][j]):
           flag=1
    if flag==0:
        c+=len(words[i])

print(c)
