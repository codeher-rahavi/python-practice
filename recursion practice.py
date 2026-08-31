def add_numbers(n):
    if n==0:
        return 0
    return n + add_numbers(n-1)

n= int(input())
ans = add_numbers(n)
print(ans)