#use seive of erithosites
def prime(n):
    arr=[True]*n
    if n<=1:
        return 0
    arr[0],arr[1]=False,False
    for i in range(2,int(n**0.5)+1):
        if arr[i]:
            for j in range(i*i,n,i):
                arr[j]=False

    return sum(arr)


print(prime(10))