def student_result(marks):
    total=0
    average=0
    highest =0

    total = sum(marks)
    average = sum(marks) / len(marks)
    highest = max(marks)

    return total , average , highest


a=int(input())
arr=[]
for i in range(a):
    b=int(input())
    arr.append(b)

result= student_result(arr)
print(result)