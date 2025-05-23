a=[1,3,2,2,4]
for i in range(0,len(a)):
    count=1
    for j in range(0,len(a)):
        if i!=j:
            if a[i]==a[j]:
                count+=1

            if count>1:
                ans=a[i]
                break

print(ans)