a=input()
b=input()
length=max(len(a),len(b))
for i in range(0,length):
    for j in range(0,length):
        if i!=j:
            if a[i]==b[j]:
                ans=a[i]

print("[",ans,"]")