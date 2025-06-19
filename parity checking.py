def oddoneout(arr):
    even_count=0
    odd_count=0

    for i in range(3):
        if arr[i]%2==0:
            even_count+=1
        else:
            odd_count+=1


    if even_count>odd_count:
        for i in arr:
            if i%2!=0:
                return i
    else:
        for i in arr:
            if i%2==0:
                return i

print(oddoneout([1, 3, 5, 2, 7]))
