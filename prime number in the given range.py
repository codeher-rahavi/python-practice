def isPrimeSeries(num):
    i=0
    while i<=num:
        flag = 0
        if i<=1:
            flag=1
        for j in range(2,(i//2)+1):
            if i%j==0:
                flag=1

        if flag==0:
            print(i)
        i+=1


n= int(input())
isPrimeSeries(n)
