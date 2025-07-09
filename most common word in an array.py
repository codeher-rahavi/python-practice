arr=[1, 2, 2, 1, 1, 3]
f = {}
for i in arr:
    if i not in f:
        f[i] = 1
    else:
        f[i] += 1

arr = []
for i in f:
    arr.append(f[i])



ans=set(arr)
if len(ans)<len(arr):
    print("False")
else:
    print("True")



