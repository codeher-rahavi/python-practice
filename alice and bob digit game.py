digits=[5,5,10]
s=0
t=0
for i in digits:
    if len(str(i))==1:
        s+=i
    else:
        t+=i
print(s,t)
if s>t or t>s:
    print("True")
else:
    print("False")
