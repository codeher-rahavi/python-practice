# ones=""
# twos=""
# threes=""
# for i in range(10):
#     ones+=str(i)
#
# for i in range(10,100):
#     twos+=str(i)
#
# for i in range(100,1000):
#     threes+=str(i)
#
# print(ones)
# print(twos)
# print(threes)
# arr=[1,2,3,4]
# arr=str(arr)
# for i in arr:
#     print(type(i))
digits=[1,2,3,4]
even_arr = []
count = 0
for i in range(100, 1000):
    if i % 2 == 0:
        even_arr.append(str(i))
ans = []
for i in even_arr:
    flag = 0
    for j in i:
        if i.count(j) > 1:
            flag = 1
            break
    if flag == 0:
        print(i)
        count += 1

print(count)