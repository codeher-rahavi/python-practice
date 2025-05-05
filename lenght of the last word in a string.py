a=input("enter a sentence:")
count=0
for i in a[-1:]:
    if(i==' '):
        break
    else:
        count=count+1

print(count)