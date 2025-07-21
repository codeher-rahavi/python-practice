def count(n):
    upper=0
    lower=0
    for i in n:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1

    return (upper,lower)

n=input()
ans=count(n)
for i in ans:
    print(i,end="\n")