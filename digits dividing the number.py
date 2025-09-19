num=121
n=str(num)
l=len(n)
c=0
for i in range(l):
    if num%int(n[i])==0:
        c+=1
print(c)