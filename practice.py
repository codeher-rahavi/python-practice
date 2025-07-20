'''
print(21+22)
print(5)
print(6/2)
print(5+3/2)

# pattern  printing using loops
for i in range(0,6):
    for j in range(0,i):
        print("*",end="\t")
    print("\n")

# printing without using loops
print("*")
print("**")
print("***")
print("****")
print("******")

print(5,5)

print(3)
print(2,end=" ")
print(32)
print("python","programming")

for i in range(0,4):
    for j in range(0,4):
        print("*" , end="")
    print("\n")

a,b=int(input()),int(input())
res=a*b
print(res)


nums=[3,2,2,3]
val=3
nums1=[]
count=0
for i in nums:
    if i != val:
        nums1.append(i)
        count=count+1

for i in range(count,len(nums)):
    nums1.append('_')

output='['+','.join(str(x) if isinstance(x,int) else '_' for x in nums1 )+ ']'

print(count,"nums=",output)
nums=[3,2,2,3]
val=3
nums1 = []
for i in nums:
    if i != val:
        nums1.append(i)

print(nums1)

print("hi","hello")'''
from operator import ifloordiv

'''
num=[1,2,3,4]
res=''.join(str(x) for x in num)
print(res)
num1=int(res)
print(num1)
num2=num1+1
result='['+','.join(x for x in str(num2))+']'
print(result)
'''
'''
a=[1,3,5,6]
t=7
i=len(a)-1
while(i>=0):
    if t>a[i]:
        print(i+1)
        break
    i-=1
'''
'''
a="   fly me   to   the moon  "
count=0
c=0
if a[-1]!=' ':
    for i in range(-1,-len(a)-1,-1):
        if(a[i]!=' '):
            count+=1
        elif(a[i]==' '):
            c=count
            break
print(c)
'''
'''
    a="   fly me   to   the moon  "
count=0
for i in range(-1,-len(a)-1,-1):
    if a[i]==' ':
        continue
    else:
        for x in range(i,-len(a)-1,-1):
            if a[x]!=' ':
                count+=1
            else:
                break
        break
print(count)
'''

#a=first.concat(" ").concat(second)
'''a = "coding on codechef"
current_count = 0
count=0
start = 0
for i in range(len(a)):
    count+=1
    if (a[i] != ' '):
        current_count += 1

    else:
        print(a[start:i], "-", current_count)
        start = i + 1
        current_count = 0

print(a[start:i],"-",current_count)


print(a, "-", count)
'''
'''
#printing string in reverse
a="I Love Python"
for i in range(-1,-len(a)-1,-1):
    print(a[i],end="")
'''
'''
# .zfill() functionality
a="11"
b=a.zfill(8)
print(b)
#output:00000011
'''
'''
#binary addition
a="11"
b="1"
n=0
z=[]
max=max(len(a),len(b))
a=a.zfill(max)
b=b.zfill(max)

for i in range(-1,-max-1,-1):
    c=int(a[i])
    d=int(b[i])
    total=c+d+n
    rem=total % 2
    n=total//2
    z.append(str(rem))

if n!=0:
    z.append(str(n))

res=''.join(reversed(z))
print(res)
'''
'''
a,b = input().split()
a=int(a)
if ((a>=18) and b=="India"):
    print("Eligible")
else:
    print("Not Eligible")

'''
'''
#square of a number
num = int(input())
i=1
while(i<=num):
    print(i*i,end=" ")
    i+=1
'''
'''
#square of a number without using built-in functions using binary search
x=9
if x == 0 or x == 1:
    print(x)

low = 1
high = x
ans = 0

while low <= high:
    mid = (low + high) // 2
    if mid * mid == x:
        print(mid)
    elif mid * mid < x:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

return ans
'''
'''
a=9
print(10//2)

'''
'''
#staircase climbing is an example of fibonnaci series
a=5
if a==1 or a==2:
    print(a)
else:
    c = 1
    b = 2
    temp = 0
    for i in range(1,a-1):
        temp = c + b
        c = b
        b = temp
print(b)
'''
#working of linked list
"""
'''the minus sign inside the string is to convert the negative number to 
positive so that there wont be an error and the negative sign is replaced again outside'''
#reversing of a number
a=1230
def reverse(n):
    if n<0:
        a= -int(str(-n)[::-1])
    else:
        a= int(str(n)[::-1])

    if a<=2**31-1 and a>=-2**31:
        return a

print(reverse(a))
"""
"""
n=["5","-2","4","C","D","9","+","+"]
arr=[]
for i in range(len(n)):
    if n[i].isdigit():
        arr.append(int(n[i]))
    elif n[i]=='C' and arr:
        arr.pop()
    elif n[i]=='D' and arr:
        arr.append(arr[-1]*2)
    elif n[i]=='+' and len(arr)>=2:
        arr.append(arr[-1]+arr[-2])

print(sum(arr))
"""
'''
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
word="234Adas"
v=0
for i in range(len(word)):
    if word[i] in vowel:
        v+=1

print(v)
'''

a="rahavi"
print(set(a))
print(b)
c=0
for i in range(len(b)):
    if b[i:] in a:
        c=len(b[i:])
        break
print(c)




