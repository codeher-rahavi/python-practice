def prime(i):
    if i <= 1:
        return False
    flag=0
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            flag=1
            break
    if i>1 and flag==0:
        return i

def comp(i):
    if i<=1:
        return False
    flag=0
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            flag=1
            break
    if i>1 and flag==1:
        return i

def numbers(n):
    pri=[]
    neg=[]
    com=[]
    for i in n:
        if prime(i) and i!=0 or i!=1:
            pri.append(i)
        elif comp(i) and i!=0 or i!=1:
            com.append(i)
        else:
            if i!=0 or i!=1:
                neg.append(i)

    return pri,com,neg
n=list(map(int,input().split()))
p,c,ne=numbers(n)
print(p)
print(c)
print(ne)
