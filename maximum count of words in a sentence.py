sentences = ["alice and bob love leetcode",
             "i think so too",
             "this is great thanks very much"]

arr=[]
for i in sentences:
    c=1
    for j in i:
        if j==' ':
            c+=1
    arr.append(c)

print(max(arr))