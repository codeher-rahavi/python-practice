def areOccurrencesEqual(s) -> bool:
    f = {}
    for i in s:
        if i not in f:
            f[i] = 1
        else:
            f[i] += 1
    arr=[]
    for i in f:
        arr.append(f[i])

    print(arr)

    a=arr[0]
    for i in range(1,len(arr)):
        if arr[i]!= a:
            return False

    return True
s="abbcc"
print(areOccurrencesEqual(s))