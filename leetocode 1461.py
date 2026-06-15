s="00110"
k=2
arr=[]
i=0
while i<len(s)-k+1:
    arr.append(s[i:i+k])
    i+=1

print(list(set(arr)))

print(len(arr) == pow(2,k))


