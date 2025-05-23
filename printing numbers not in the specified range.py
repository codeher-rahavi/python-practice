a= [2,2]
arr2=[]
for i in range(1,len(a)+1):
    arr2.append(i)

ans=[]
for i in arr2:
    if i not in a:
        ans.append(i)

print(ans)