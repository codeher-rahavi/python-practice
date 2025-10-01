num=3
t=2
a=0
arr=[num-t,num,num+t]
ans=max(arr)
for i in range(num+1000):
    if i-t == ans:
        a=i
        break
print(arr)
print(a)