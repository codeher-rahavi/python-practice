def reverse_number(n,b):
    if n==0:
        return b
    else:
        last_digit = n%10
        b+=str(last_digit)
        n//=10
        return reverse_number(n,b)


a = int(input())
b=''
ans = reverse_number(a,b)
print(ans)