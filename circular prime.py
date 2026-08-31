def circularPrime(n):
    l=len(str(n))-1
    num=n
    flag=0
    while True:
        rem= num%10
        a=num//10
        rem = rem * pow(10,l)
        num = rem +a

        if num<=1:
            flag=1
        for i in range(2,(num//2)+1):
            if num % i==0:
                flag = 1

        if num==n:
            break

    if flag==0:
        print("Circular Prime")
    else:
        print("Not a circular prime")




n=int(input())
circularPrime(n)

4