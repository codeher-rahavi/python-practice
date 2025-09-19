arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
f={}
for i in arr1:
    if i not in f:
        f[i]=1
    else:
        f[i]+=1

ans=[]
for i in list(f.keys()):
    if i not in arr2:
        del f[i]

print(f)
for i,j in f.items():
    ans.extend([i]*j)

arr=[]
#have to look into this program another time tata bye bye
