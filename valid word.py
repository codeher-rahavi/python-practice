word="b3"
c = 0
v = 0
d = 0
n=0
if len(word) < 3:
    print("False")
else:
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(word)):
        if (word[i] in vowel) and (word[i].isalpha()):
            v+=1
        elif word[i].isalpha():
            c+=1
        elif word[i].isnumeric():
            d+=1
        else:
            print("False")


print(c,v,d)
if c >= 1 and v >= 1 and d >= 1 and n==0:
    print("true")
else:
    print("false")




