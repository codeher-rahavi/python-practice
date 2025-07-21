s="aab"
arr=[]
for i in s:
    if len(arr)<2:
        arr.append(i)
    elif arr[len(arr)-1]==arr[len(arr)-2] and i==arr[len(arr)-2]:
        continue
    else:
        arr.append(i)
ans=''.join(arr)
print(ans)