def validate_password(password):
    length=False
    uppercase=False
    digit=False
    special=False

    if len(password) >=8:
        length=True
    for i in range(len(password)):
        if password[i] >='A' and password[i]<='Z':
            uppercase=True
        elif password[i]>='0' and password[i]<='9':
            digit=True
        elif not ((password[i] >='A' and password[i]<='Z' )
                            and (password[i] >='a' and password[i]<='z')
                            and (password[i] >='0' and password[i]<='9')):
            special=True

    return {
        "length":length,
        "uppercase":uppercase,
        "digit":digit,
        "special":special
    }
n=input()
ans = validate_password(n)
print(ans)
