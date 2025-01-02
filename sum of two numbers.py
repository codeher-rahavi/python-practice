a=int(input("enter array size:"))
b=[]
for i in range(a):
    c=int(input())
    b.append(c)
d=int(input("enter a target number:"))
found=False
for i in range(0,a):
    for j in range(i+1,a):
        if b[i]+b[j]==d:
            print("[", i, "," ,j,"]")
            found=True
if not found:
    print("No pairs found that sum to the target.")