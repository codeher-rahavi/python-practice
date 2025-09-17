score = [10,3,8,9,4]
sort=sorted(score,reverse=True)
f={}
for i,j in enumerate(sort):
    if i==0:
        f[j]="Gold Medal"
    elif i==1:
        f[j]="Silver Medal"
    elif i==2:
        f[j]="Bronze Medal"
    else:
        f[j]=str(i+1)
arr=[]
for i in sort:
    arr.append(f[i])

print(arr)