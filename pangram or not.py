a="thequickbrownfoxjumpsoverthelazydog"
freq=[0]*26

for i in range(0,len(a)):
    index=ord(a[i])-ord('a')
    if freq[index]==0:
        freq[index]+=1

flag=1
for i in range(0,26):
    if freq[i]==0:
        flag=0
        break

if flag==0:
    print("Not a pangram")
else:
    print("It is a pangram")