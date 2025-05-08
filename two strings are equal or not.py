word1=['ab','c']
word2=['a','bc']
new1=''
new2=''
for i in word1:
    new1=new1+i

for i in word2:
    new2=new2+i

if new1==new2:
    print("true")
else:
    print("False")