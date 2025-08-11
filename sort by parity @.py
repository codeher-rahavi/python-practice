nums=[4,2,5,7]
e=[]
o=[]
arr=[]
for i in nums:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
k=0
m=0
for i in range(len(nums)):
    if i%2==0:
        arr.append(e[k])
        k+=1
    else:
        arr.append(o[m])
        m+=1

print(arr)