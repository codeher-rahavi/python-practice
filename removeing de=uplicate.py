a="haai how are you"
b=a[0]
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        continue
    else:
        b+=a[i]


if a==b:
    print("no duplicate found")
else:
    print(b)