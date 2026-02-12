s ="leeeeetcode"
t ="yyyyylyyyyyyeyyyyyeyyyyyyyeyyyyyyyyeyyyyyyyyeyyyyyyyytyyyycyyyyyyoyyydyyyyyyyeyyyy"
a=''
for i in t:
    if i in s:
        a+=i
print(a)
if a == s:
    print("True")
elif s in a:
    print("True")
else:
    print("False")

