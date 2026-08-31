def primeFactors(n):
    while n%2==0:
        print(2,end=" ")
        n//=2

    i=3
    while i*i <=n:
        while n%i==0:
            print(i,end=" ")
            n//=i

    if n>2:
        print(n)

n=int(input())
primeFactors(n)

