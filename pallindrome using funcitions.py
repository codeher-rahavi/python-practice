def pallindrome(string):
    l=len(string)
    b=''
    for i in range(l-1,-1,-1):
        b+=string[i]

    if string == b:
        print("True")
    else:
        print("False")

str= input()
pallindrome(str)