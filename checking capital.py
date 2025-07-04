s="Ukj"
if s.isupper():
    print("True")
elif s.islower():
    print("True")
elif s[0].isupper() and s[1:].islower():
    print("True")
else:
    print("False")