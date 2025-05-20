a=input("enter a roman numeral:")
roman={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}
prev=0
total=0
i=len(a)-1
while i>=0:
    num=roman[a[i]]
    if num<prev:
        total=total-num
    else:
        total=total+num
        prev=num
    i-=1

print(total)
