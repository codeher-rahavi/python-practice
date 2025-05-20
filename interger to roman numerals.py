a=9
roman=[
    'M','CM','D','CD',
    'C','XC','L','XL',
    'X','IX','V','IV','I'
]
numbers=[
    1000,900,500,400,
    100,90,50,40,
    10,9,5,4,1
]
count=0
rom=""
i=0
while a>0:
    count =a //numbers[i]
    rom+=roman[i]*count
    a-=numbers[i]*count
    i+=1

print(rom)