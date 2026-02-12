words= ["i","love","leetcode","i","love","coding"]
k = 3
f={}
for i in words:
    f[i] = words.count(i)
s  = sorted(f.items(), key=lambda item: (-item[1],item[0]))
arr=[]
print(s)

for i in s:
    arr.append(i[0])

print(arr[:k])