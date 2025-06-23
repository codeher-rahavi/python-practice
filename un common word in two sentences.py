s1 = "this apple is sweet"
s2 = "this apple is sour"
total=s1.split()+s2.split()
freq={}
for i in total:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
arr=[]
for i in freq:
    if freq[i]==1:
        arr.append(i)
print(arr)