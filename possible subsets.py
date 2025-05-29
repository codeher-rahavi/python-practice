a=[1,2,3]
res=[[]]
for i in a:
    arr=[]
    for j in res:
        arr.append(j+[i])
    res.extend(arr)

print(res)


