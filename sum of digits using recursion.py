def sum_of_nums(n,s):
    if n==0:
        return s
    else:
        last_digit = n%10
        s += last_digit
        n//=10
        return sum_of_nums(n,s)

a = int(input())
s=0
ans = sum_of_nums(a,s)
print(ans)