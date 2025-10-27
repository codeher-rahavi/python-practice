s="34789"
num=''
while(True):
    for i in range(0,len(s)-1):
        num+=(str((int(s[i])+int(s[i+1]))%10))
    s=num
    num=''
    if(len(s)==2):
        break


print(s)
if len(s)==2 and s[0]==s[1]:
    print("true")
else:
    print('false')