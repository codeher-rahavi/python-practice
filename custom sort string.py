order ="hucw"
s ="utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"
s=list(s)
b=''
d=set()
for i in order:
    if i in s :
        b+=i * s.count(i)

for i in s:
    if i not in b:
        b+=i * s.count(i)
print(b)

