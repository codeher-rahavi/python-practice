def odd_even(n):
    if n%2 == 0:
        return True
    else:
        return False

a=int(input("Enter a number:"))
ans = odd_even(a)
if ans:
    print("Even")
else:
    print("Odd")