num=int(input())
for i in range(0,num):
    if num==pow(3,i):
        print("True")
        break
    elif pow(3,i)>num:
        print("False")

