def number_analyser(numbers):
    even=0
    odd=0
    total=0
    largest=0
    l=len(numbers)
    for i in range(l):
        if i %2==0:
            even+=1
        else:
            odd+=1

    total = sum(numbers)
    largest = max(numbers)

    return {
        "even": even,
        "odd": odd,
        "sum": sum(numbers),
        "largest": max(numbers)
    }


a=int(input())
arr=[]
for i in range(a):
    b=int(input())
    arr.append(b)

ans = number_analyser(arr)
print(ans)