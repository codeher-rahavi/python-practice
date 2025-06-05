nums=[-1,-2]
k=2
freq={}
for i in nums:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1

sort=dict(sorted(freq.items() ,key=lambda item:item[1],reverse=True))

print(sort)
arr=[]
count=1
for i in sort:
    if count<=k:
        arr.append(i)
        count+=1

print(arr)