def check_password(password):
    score = 0
    l=len(password)
    if l>=8: score+=1

    for i in range(l):
        if password[i] >='A' and password[i]<='Z':
            score+=1
            break
    for i in range(l):
        if password[i] >= '0' and password[i] <='9':
            score+=1
            break
    for i in range(l):
        if not((password[i] >='A' and password[i] <='Z') or
               (password[i] >='a' and password[i]<='z') or
               (password[i] >='0' and password[i] <='9')):
                score+=1
                break

    status ='Strong' if score==4 else 'Weak'

    return score,status

str=input()
ans = check_password(str)
print(ans)

