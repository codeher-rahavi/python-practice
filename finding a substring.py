a=input("enter a string:")
b=input("enter a substring to find:")
count=0
for i in range(len(a)-len(b)+1):
    if a[i:i+len(b)]==b:
        count+=1
print(b,"occurs",count,"times")