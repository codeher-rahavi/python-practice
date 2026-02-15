nums = ["0","0"]
k = 2
num=[]
for i in nums:
    num.append(int(i))

num.sort(reverse=True)
for i in range(len(num)):
    if i+1 == k:
        print(str(num[i]))


