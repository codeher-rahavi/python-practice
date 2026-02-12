word ="AbBCab"
l=[-1]*26
u=[-1]*26
for i in range(len(word)):
    if word[i].islower():
        l[ord(word[i])-97] = i

flag=[0]*26

for j in range(len(word)):
    if word[j].isupper() and flag[ord(word[j]) - 65]!=1:
        u[ord(word[j])-65] = j
        flag[ord(word[j]) -65] = 1

count=0
for i in range(26):
    if l[i]!=-1 and u[i]!=-1 and l[i]<u[i] :
        count+=1


print(count)




