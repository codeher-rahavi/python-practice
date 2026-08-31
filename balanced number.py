def balance(n,p,arr):
    hard = p//10
    cake = p//2

    h=0
    c=0

    for i in arr:
        if i<=hard:
            h+=1
        if i>=cake:
            c+=1

    if h==2 and c==1:
        print("yes")
    else:
        print("no")

n, p = map(int,input().split())
arr =  list(map(int,input().split()))
balance(n,p,arr)